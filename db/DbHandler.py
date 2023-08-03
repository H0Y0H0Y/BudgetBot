from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from bson.objectid import ObjectId
from constants import MONGODB_CONN_STRING, DB

class DbHandler:

    def __init__(self, conn_string: str = MONGODB_CONN_STRING, db: str = DB) -> None:
        self.client: MongoClient = MongoClient(conn_string)
        self.db: Database = self.client[db]
    
    def find_record(self, collection: Collection, query: dict) -> dict:
        return collection.find_one(query)
    
    def insert_record(self, collection: Collection, record: dict) -> ObjectId:
        result = collection.insert_one(record)
        return result.inserted_id