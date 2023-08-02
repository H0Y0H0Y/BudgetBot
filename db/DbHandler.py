from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from constants import MONGODB_CONN_STRING, DB

class DbHandler:

    def __init__(self, conn_string: str = MONGODB_CONN_STRING, db: str = DB) -> None:
        self.client: MongoClient = MongoClient(conn_string)
        self.db: Database = self.client[db]
    
    def find_record(self, collection: Collection, query: dict) -> dict:
        return collection.find_one(query)