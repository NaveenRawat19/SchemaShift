from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("db_username")
password = os.getenv("db_password")
cluster_name = os.getenv("cluster_name")

uri = f"mongodb+srv://{username}:{password}@{cluster_name}.upqcacu.mongodb.net/?retryWrites=true&w=majority&appName={cluster_name}"
client = MongoClient(uri, server_api=ServerApi('1'), tls=True)

class dbService:
    def __init__(self):
        pass
    
    def get_exercises(self):
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")

            data = client["exercises"]  # Example operation, adjust as needed
            exercises = data["reps"]  # Example collection, adjust as needed
            reps = list(exercises.find({}))  # Convert cursor to list for returning

            for doc in reps:
                doc["_id"] = str(doc["_id"])
            return reps

        except Exception as e:
            print(e)
    
    def get_users(self):
        try:
            db = client["users"]
            users_collection = db["users"]
            users = list(users_collection.find({}))
            for user in users:
                user["_id"] = str(user["_id"])
            return users
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def add_user(self, user):
        try:
            db = client["users"]
            users_collection = db["users"]
            users_collection.insert_one(user.dict())
            return {"status": "success", "message": "User added successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}