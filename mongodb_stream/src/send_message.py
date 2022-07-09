import os
import pymongo
import json

parameters = json.loads(open('../env_config.json').read())
connection_str = parameters['CHANGE_STREAM_DB']
client = pymongo.MongoClient(connection_str)
print(client.changestream.collection.insert_one({"hello": "TRV"}).inserted_id)
