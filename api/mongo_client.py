import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")

MONGO_URL = os.environ.get("MONGO_URL","mongo")
MONGO_USERNAME= os.environ.get("MONGO_USERNAME","root")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD","gursheen")
MONGO_PORT = os.environ.get("MONGO_PORT",27017)


mongoClient = MongoClient(
host = MONGO_URL,
username= MONGO_USERNAME,
password= MONGO_PASSWORD,
port = MONGO_PORT

)

def insert_test_document():
    db= mongoClient.test
    test_collection = db.test_collection
    res=test_collection.insert_one({"name":"gursheen","age":"26"})
    dummy_col = db.dummy_col
    res1=dummy_col.insert_one({"name":"gursheen"})
    

    # db1= mongoClient.dummy
    # dummy_col = db1.dummy_col
    # res1=dummy_col.insert_one({"name":"gursheen"})
    # print(res1)