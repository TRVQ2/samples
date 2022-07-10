import os
import pymongo
import json
from bson.json_util import dumps

parameters = json.loads(open('../env_config.json').read())
connection_str = parameters['CHANGE_STREAM_DB']
client = pymongo.MongoClient(connection_str)
# for x in client.changestream.collection.find():  # listing all data
#    print(x)
change_stream = client.changestream.collection.watch()
for change in change_stream:
    print(dumps(change), '\n')
