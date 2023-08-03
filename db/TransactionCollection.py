from pymongo.collection import Collection
from bson.objectid import ObjectId
from db.DbHandler import DbHandler

class TransactionCollection(DbHandler):

    def __init__(self) -> None:
        super().__init__()
        self.collection: Collection = self.db["transactions"]
    
    def find_transaction(self, query: dict) -> dict:
        return super().find_record(self.collection, query)
    
    def insert_transaction(self, record: dict) -> ObjectId:
        return super().insert_record(self.collection, record)