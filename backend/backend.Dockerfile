# https://fastapi.tiangolo.com/tr/deployment/docker/#build-a-docker-image-for-fastapi
# 
FROM python:3.10
# 
WORKDIR /app
#
COPY backend/requirements.txt /app
# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# 
# Install Tesseract for PyMuPDF
# RUN apt-get update && apt-get install tesseract-ocr -y
# RUN apt-get install tesseract-ocr-por
#
# ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata
#
# ADD /backend_modules /app
# 
ADD /backend/src /app
# 
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

# # https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9 AS INICIAL
# ADD requirements.txt /app
# RUN pip install --no-cache-dir --upgrade -r requirements.txt

# FROM INICIAL 
# ADD . /app

# Substitui para um multi-stage build para acelerar o rebuild no desenvolvimento:

# Uso a imagem disponível no dockerhub para o servidor web uvicorn
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 
# ADD . /app
# RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
# Assim, o que vocẽ construiu na máquina de desenvolvimento (host) estará disponível dentro do container
# Dentro do container, tudo estára no diretório /app
# Isto é uma cópia, não um mapeamento dinâmico. A imagem fica independente do host original.

#Para criar a imagem

    #docker build -t rfb_ceiamin_backend .

#Para abrir o container sem rodar nada e obter um prompt. Você pode usar ls para ver a estrutura dentro do container

    #docker run -it rfb_ceiamin_backend /bin/bash

#Para sair digite

    # exit

# Para rodar o container digite

#docker run  -p 8001:80 --name c_rfb_ceiamin_backend --rm rfb_ceiamin_backend

#Note que na máquina host o serviço estara disponível na porta 8001, mas o servidor web, está atendendo na porta 80
#dentro do container. o "-p", faz o mapeamento.
#O --name define o nome do container que é c_rfb_ceiamin_backend
#O rfb_ceiamin_backend é o nome da imagem
#O container pode ser parado e depois continuar após ter alterado seu estado interno.
#Então container != imagem
#Quando o container é parado, por um ^C ou por um

    # docker stop  c_rfb_ceiamin_backend

#ele continuaria existindo. Você poderia reativá-lo com

    # docker start c_rfb_ceiamin_backend

#poŕem, coloquei a diretiva -rm no comando para eliminar o container.
#Fiz isto para começar do zero de novo com outro docker run
#Se o container já existe, o docker run não funmciona.


# para colocar imagem no dockerhub, se quiser

    #docker login --username=seu_usuario_no_docker_hub
    #docker tag rfb_ceiamin_backend seu_usuario_no_docker_hub/seu_repositorio:rfb_ceiamin_backend
    #docker push rfb_ceiamin_backend seu_usuario_no_docker_hub/seu_repositorio:rfb_ceiamin_backend

# Em qualquer outro lugar você pode pegar a imagem e se o repositório for público, qualquer um pode

    #sudo docker pull rfb_ceiamin_backend seu_usuario_no_docker_hub/seu_repositorio:rfb_ceiamin_backend

#Tendo obtido a imagem, ele pode ser executada, não é preciso ter o código fonte para cria a imagem de novo
#Ela vem com tudo

#Se você clonar o repositório do git, aí você não precisa pegar a imagem, pode reconstruí-la onde estiver.