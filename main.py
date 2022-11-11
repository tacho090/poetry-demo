from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster25583.uxocfmt.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test
