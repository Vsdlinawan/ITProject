import pymongo

class PythonToMongo:
    def __init__(self, strConnection, strDatabase, strCollection):
        self.client = pymongo.MongoClient(strConnection)
        self.db = self.client[strDatabase]
        self.collection = self.db[strCollection]
    
    # WORKING
    def insert(self, data, collection_Name = None):
        if collection_Name == None:
            collection_Name = self.collection.name 
        collection = self.db[collection_Name]
        collection.insert_one(data)
        print(f"Inserted to {self.db.name} {collection_Name}")
        
    # WORKING
    def find_one(self, data:dict):
        return self.collection.find_one(data)
    
    def find(self, data:dict = {}, collection_Name = None):
        if collection_Name == None:
            collection_Name = self.collection.name 
        collection = self.db[collection_Name]
        return collection.find(data)
    
    def delete(self, data:dict, collection_Name = None):
        print(f"Deleted to {self.db.name} {self.collection.name}")
        if collection_Name == None:
            collection_Name = self.collection.name 
        collection = self.db[collection_Name]
        return collection.delete_one(data)
    
    def modify(self, data:dict, newValue:dict):
        print(f"Modified to {self.db.name} {self.collection.name}")
        return self.collection.update_one(data, newValue)