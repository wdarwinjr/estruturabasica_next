openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./selfsigned.key -out ./selfsigned.crt
# python ceia.py
# cd backend
# docker build -t rfb_ceia_backend .
# cd ..
# cd frontend
# docker build -t rfb_ceia_frontend .
# export ENV_FOR_DYNACONF=testing
# docker-compose up
