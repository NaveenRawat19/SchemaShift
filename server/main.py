from fastapi import FastAPI, Depends
import sys, os
from services.exersizeService.exersize import ExersizeService
import json, subprocess
from server.models.models import User, UserAuth
from auth.kerberos_auth import KerberosAuth

app = FastAPI()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@app.get("/")
async def root():
    with open("db/exercises.json", "r") as file:
        data = json.load(file)
    if data and isinstance(data, list) and data[0]:
        keys = list(data[0].keys())
        return {"keys": keys}
    else:
        return {"keys": []}

@app.post("/authenticate")
async def authenticate(user_auth: UserAuth):
    auth = KerberosAuth()
    return auth.authenticate(user_auth.username, user_auth.password)

@app.get("/get-exercises")
async def get_exercises():
    exercise = ExersizeService()
    return exercise.process()

@app.get("/get-users")
async def get_users():
    exercise = ExersizeService()
    return exercise.db.get_users()

@app.post("/users/add")
async def add_user(payload: User):
    exercise = ExersizeService()
    return exercise.db.add_user(payload)
                
    
