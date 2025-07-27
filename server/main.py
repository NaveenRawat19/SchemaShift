from fastapi import FastAPI, File, UploadFile
from services.dbMigration.migrationService import MigrationService
import json, subprocess
import tempfile
app = FastAPI()

@app.get("/")
async def root():
    with open("db/exercises.json", "r") as file:
        data = json.load(file)
    if data and isinstance(data, list) and data[0]:
        keys = list(data[0].keys())
        return {"keys": keys}
    else:
        return {"keys": []}
    
@app.post("/nosql-to-sql")
async def convert_nosql_to_sql(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name

        migrate = MigrationService(db_connection=None, source_collection=temp_file_path, target_table="target_table")
        keys = migrate.migrate()
        return keys
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}, 400
                
    
