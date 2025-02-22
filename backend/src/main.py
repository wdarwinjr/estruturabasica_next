from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from models import *
import os
import sys

# from database.dbqueries import copySubDBBasico

# Importação de Módulos Python do backend_modules:
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
grandparent_directory = os.path.dirname(parent_directory)
sys.path.append(grandparent_directory+"/backend_modules")

from modules.ferramentas_mongodb import get_database
# from ferramentas_json import *
# from totalizar import *



if "NOIAPATH" in os.environ and os.environ["NOIAPATH"]:
    app = FastAPI()
else:
    app = FastAPI(root_path="/backend")


from routes.hashes import router as HashesRouter
# from routes.iprocs import router as PalavrasChaveRouter
# from routes.conjuntos import router as ConjuntosRouter
# from routes.agrupamentos import router as AgrupamentosRouter
# from routes.docs import router as PDFsRouter
# from routes.config import router as ConfigRouter
# from routes.root import router as RootRouter
# from routes.token import router as TokenRouter
# from routes.processamento import router as ProcessamentoRouter

# from ferramentas_json import router as FerramentasJSONRouter
# from totalizar import router as TotalizarRouter
# from root import router as ModuleRouter


app.include_router(HashesRouter, tags=["Hashes"], prefix="/hashes")
# app.include_router(ConjuntosRouter, tags=["Conjuntos"], prefix="/conjuntos")
# app.include_router(AgrupamentosRouter, tags=["Agrupamentos"])
# app.include_router(ProcessamentoRouter, tags=["Processamento"])
# app.include_router(TotalizarRouter, tags=["Totalizar"])
# app.include_router(FerramentasJSONRouter, tags=["FerramentasJSON"])
# app.include_router(PalavrasChaveRouter, tags=["PalavrasChave"], prefix="/iprocesso")
# app.include_router(PDFsRouter, tags=["PDFs"], prefix="/iprocesso")
# app.include_router(ConfigRouter, tags=["Config"], prefix="/config")
# app.include_router(RootRouter, tags=["Root Test"])
# app.include_router(TokenRouter, tags=["Token Test"])
# app.include_router(ModuleRouter, tags=["Module Test"])
# app.include_router(ApitasksRouter, tags=["API Tasks Test"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# async def initial_index(mdb: AsyncIOMotorClient):
#     mdb.documentos.create_index([("arquivo", 1)], unique=True)
#     mdb.documentos.create_index([("tipoDoDocumento", 1)])
#     mdb.documentos.create_index([("Subtipo", 1)])
#     mdb.documentos.create_index([("numeroDoProcesso", 1)])
#     mdb.documentos.create_index([("paginaFinal", 1)])
#     mdb.documentos.create_index([("uniqueID", 1)], unique=True)
#     mdb.conjuntos.create_index([("nomeDoConjunto", 1)], unique=True)
#     mdb.conjuntos.create_index([("processosDoConjunto", 1)])
#     mdb.agrupamentos.create_index([("idDoConjunto", 1)])
#     mdb.jsonfisicos.files.create_index([("filename", 1)], unique=True)
#     mdb.jsonlogicos.files.create_index([("filename", 1)], unique=True)
#     mdb.jsonlimpos.files.create_index([("filename", 1)], unique=True)
#     mdb.pdfsgridfs.files.create_index([("filename", 1)], unique=True)
#     mdb.palavraschave.create_index([("numeroDoProcesso",1)], unique=True)


@app.on_event("startup")
async def startup():
    app.mongodb_client = await get_database()
    # indexados = await initial_index(app.mongodb_client)
    # conjuntos_list = ['teste_paragrafos_procs', 'Amostra OEA']
    # await copySubDBBasico(conjuntos_list, prior_drop=False)


# @app.on_event("shutdown")
# async def shutdown():
#     app.mongodb_client.close()
# from root import router as ModuleRouter