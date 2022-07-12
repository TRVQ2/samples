import os
import pymongo
import json
from bson.json_util import dumps


parameters = json.loads(open('../env_config.json').read())
client = pymongo.MongoClient(parameters['CONNECTION_STR'])
db = client[parameters['DB_NAME']]
collection = db[parameters['COLLECTION']]
change_stream = collection.watch()
for change in change_stream:
    print(dumps(change), '\n')
