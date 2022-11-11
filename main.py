import os

from dotenv import load_dotenv
from pymongo import MongoClient


MONGO_ATLAS_URI = os.environ.get("MONGO_ATLAS_URI")
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME")
MONGO_PASSWORD = os.environ.get("MONGO_DB_PASSWORD")
MONGO_DB_USERNAME = os.environ.get("MONGO_DB_USERNAME")

load_dotenv()
client = pymongo.MongoClient(f"mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_PASSWORD}@cluster25583.uxocfmt.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test
