from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
import hashlib
import os

# Importação de Módulos Python do backend_modules:
# current_directory = os.getcwd()
# parent_directory = os.path.dirname(current_directory)
# grandparent_directory = os.path.dirname(parent_directory)
# sys.path.append(grandparent_directory+"/backend_modules")

from modules.ferramentas_mongodb import get_database

local_IP = os.environ["LOCAL_IP"]

router = APIRouter()

def gerar_hash(valor: str) -> str:
    # Usando SHA-256 para hash.
    return hashlib.sha256(valor.encode()).hexdigest()


@router.post("/criar-hash/")
async def criar_hash(nome_usuario: str, cpf: str, mdb: AsyncIOMotorClient = Depends(get_database)):
    usuario_hash = gerar_hash(nome_usuario)
    cpf_hash = gerar_hash(cpf)
    
    # Criação de um documento para armazenar no MongoDB
    documento = {
        "nome_usuario": nome_usuario,
        "cpf": cpf,
        "usuario_hash": usuario_hash,
        "cpf_hash": cpf_hash
    }
    
    # Inserção do documento na collection 'hashes'
    mdb.hashes.insert_one(documento)
    
    return {"usuario_hash": usuario_hash, "cpf_hash": cpf_hash}


@router.get("/verificar-hash/")
async def verificar_hash(usuario_hash: str, cpf_hash: str, mdb: AsyncIOMotorClient = Depends(get_database)):
    # Verifica se existe algum documento com os hashes fornecidos
    resultado = await mdb.hashes.find_one({"usuario_hash": usuario_hash, "cpf_hash": cpf_hash})
       
    if resultado:
        # Retorna o nome de usuário e CPF do documento encontrado
        return {
            "valido": True,
            "nome_usuario": resultado["nome_usuario"],
            "cpf": resultado["cpf"]
        }
    else:
        raise HTTPException(status_code=404, detail="Hashes não encontrados.")
    

@router.post("/gerar-hash-e-url/")
async def gerar_url_com_hash(nome_usuario: str, cpf: str, mdb: AsyncIOMotorClient = Depends(get_database)):
    hash_response = await criar_hash(nome_usuario, cpf, mdb)
    usuario_hash = hash_response["usuario_hash"]
    cpf_hash = hash_response["cpf_hash"]
    
    # Construir a URL com os hashes
    url_com_hash = f"https://{local_IP}/?usuario_hash={usuario_hash}&cpf_hash={cpf_hash}"
    
    return {"url": url_com_hash}


@router.get("/obter-url-por-hash/")
async def obter_url_por_hash(usuario_hash: str, cpf_hash: str, mdb: AsyncIOMotorClient = Depends(get_database)):
    # Verifica se existe algum documento com os hashes fornecidos
    resultado = await mdb.hashes.find_one({"usuario_hash": usuario_hash, "cpf_hash": cpf_hash})
        
    if resultado:
        # Se os hashes forem encontrados, constrói a URL com os hashes
        url_com_hash = f"https://{local_IP}/?usuario_hash={usuario_hash}&cpf_hash={cpf_hash}"
        return {"url": url_com_hash}
    else:
        # Se os hashes não forem encontrados, retorna um erro
        raise HTTPException(status_code=404, detail="Hashes não encontrados.")


@router.get("/obter-url-por-login/")
async def obter_url_por_login(nome_usuario: str, cpf: str, mdb: AsyncIOMotorClient = Depends(get_database)):
    # Verifica se existe algum documento com os hashes fornecidos
    resultado = await mdb.hashes.find_one({"nome_usuario": nome_usuario, "cpf": cpf})
        
    if resultado:
        # Se os hashes forem encontrados, constrói a URL com os hashes
        url_com_hash = f"https://{local_IP}/?usuario_hash={resultado['usuario_hash']}&cpf_hash={resultado['cpf_hash']}"
        return {"url": url_com_hash}
    else:
        # Se os hashes não forem encontrados, retorna um erro
        raise HTTPException(status_code=404, detail="Hashes não encontrados.")