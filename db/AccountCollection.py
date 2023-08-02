from pymongo.collection import Collection
from db.DbHandler import DbHandler

class AccountCollection(DbHandler):

    def __init__(self) -> None:
        super().__init__()
        self.collection: Collection = self.db["accounts"]
    
    def find_account(self, query: dict) -> dict:
        return super().find_record(self.collection, query)