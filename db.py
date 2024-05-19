import os
from pymongo import MongoClient


CONNECTION_STRING = os.environ.get("AZURE_COSMOS_CONNECTIONSTRING")
client: MongoClient = MongoClient(CONNECTION_STRING)
db = client.get_database("db_todo")
