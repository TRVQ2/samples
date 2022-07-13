import os
import pymongo
import json

with open('../env_config.json', 'r') as f:
    parameters = json.loads(f.read())
client = pymongo.MongoClient(parameters['CONNECTION_STR'])
db = client[parameters['DB_NAME']]
collection = db[parameters['COLLECTION']]
record = collection.find_one()
print(record)
# print(collection.insert_one({"test": "test"}).inserted_id)
# filter = {"_id": record["_id"]}
# collection.update_one(filter, {"$set": {"test": None}})
