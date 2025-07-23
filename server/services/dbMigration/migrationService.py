import json

class MigrationService:
    def __init__(self, db_connection, source_collection, target_table):
        self.db_connection = db_connection
        self.source_db = source_collection
        self.target_db = target_table
    
    def migrate(self):
        # This method should implement the logic to migrate data from a NoSQL collection
        # to a SQL table. The implementation will depend on the specific database systems
        # and libraries used.
        result = []

        data = json.loads(self.source_db)
        for d in data:
            for key, value in d.items():
                new_dict = {"key": key, "type": type(value).__name__}
                print(new_dict)
                result.append(new_dict)
        
        return result                   