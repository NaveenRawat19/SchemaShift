import json
from db.db import dbService

class ExersizeService:
    def __init__(self):
        self.db = dbService()
    
    def process(self):
        return self.db.get_exercises()
    
    def get_users(self):
        try:
            return self.db.get_users()
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def add_user(self, user):
        try:
            return self.db.add_user(user)
        except Exception as e:
            return {"status": "error", "message": str(e)}