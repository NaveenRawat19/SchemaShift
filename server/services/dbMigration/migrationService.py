import json

class MigrationService:
    def __init__(self, db_connection, source_collection, target_table):
        self.db_connection = db_connection
        self.source_db = source_collection
        self.target_db = target_table
        self.parent = None
    
    def migrate(self):
        result = []
        print(f"Data loaded from {self.source_db}")
        with open(self.source_db, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print("inside migrationService")
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        result.extend(self.process_json(item))
                    else:
                        print("Warning: List item is not a dict, skipping:", item)
            elif isinstance(data, dict):
                result = self.process_json(data)
            else:
                print("Unsupported JSON root type:", type(data))
        print(data)
        return result   

    def process_json(self, json_object):
        columns = []
        foreign_keys = []
        create_table_sql = []
        # Always create an id
        columns.append("id INTEGER PRIMARY KEY AUTOINCREMENT")

        if self.parent:
            columns.append(f"{self.parent}_id INTEGER")
            foreign_keys.append(f"FOREIGN KEY ({self.parent}_id) REFERENCES {self.parent}(id)")
        
        for key, value in json_object.items():
            if isinstance(value, dict):
                # Nested object: create new table recursively
                child_table_sql = self.process_json(value)
                create_table_sql.extend(child_table_sql)
                columns.append(f"{key}_id INTEGER")
                foreign_keys.append(f"FOREIGN KEY ({key}_id) REFERENCES {key}(id)")
            elif isinstance(value, list):
                # Array: create a separate table for list items
                if value and isinstance(value[0], dict):
                    for item in value:
                        child_table_sql = self.process_json(item)
                        create_table_sql.extend(child_table_sql)
                else:
                    columns.append(f"{key} TEXT")  # Or your chosen representation
            else:
                columns.append(f"{key} TEXT")  # Adjust type as appropriate

        # Compose CREATE TABLE statement
        statement = f"CREATE TABLE {self.target_db} (\n  " + ",\n  ".join(columns + foreign_keys) + "\n);"
        create_table_sql.append(statement)
        return create_table_sql              