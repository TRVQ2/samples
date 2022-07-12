import os
import pymongo
import json

parameters = json.loads(open('../env_config.json').read())
client = pymongo.MongoClient(parameters['CONNECTION_STR'])
db = client[parameters['DB_NAME']]
collection = db[parameters['COLLECTION']]
record = collection.find_one()
print(record)
# print(collection.insert_one({"test": "test"}).inserted_id)
# filter = {"_id": record["_id"]}
# collection.update_one(filter, {"$set": {"test": None}})
