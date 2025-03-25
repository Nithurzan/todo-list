import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://plant:plant@plant.jw95g.mongodb.net/?retryWrites=true&w=majority&appName=plant")
client = AsyncIOMotorClient(MONGO_URI)
db = client.todo_db


users_collection = db.users 
todos_collection = db.todos