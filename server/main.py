from fastapi import FastAPI, File, UploadFile
from services.dbMigration.migrationService import MigrationService
import json, subprocess

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
    output_json = "output.json"
    try:
        content = subprocess.run(
            ["bsondump", "--outFile=" + output_json, file],
            capture_output=True,
            text=True
        )
        migrate = MigrationService(db_connection=None, source_collection=content, target_table="target_table")
        keys = migrate.migrate()
        return keys
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}, 400
                
    
