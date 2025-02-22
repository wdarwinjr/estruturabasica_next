from motor.motor_asyncio import AsyncIOMotorClient
import os

with open(os.environ["MONGO_INITDB_ROOT_PASSWORD_FILE"]) as f:
    MONGO_DB_PASSWORD = f.readline()

async def get_client():
    client = AsyncIOMotorClient(
        os.environ["MONGO_DB_HOST"], 
        int(os.environ["MONGO_DB_PORT"]), 
        username=os.environ["MONGO_DB_USER"], 
        password=MONGO_DB_PASSWORD)
    return client

async def get_database():
    client = AsyncIOMotorClient(
        os.environ["MONGO_DB_HOST"], 
        int(os.environ["MONGO_DB_PORT"]), 
        username=os.environ["MONGO_DB_USER"], 
        password=MONGO_DB_PASSWORD)
    return client.fiscalizacao
