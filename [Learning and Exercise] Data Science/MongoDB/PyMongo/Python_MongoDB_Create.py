# Python_MongoDB_Create.py

from pymongo import MongoClient

# Step 1: Initialize MongoClient:
myclient = MongoClient('localhost', 27017)
print('creating session: ', myclient.list_database_names())

# Step 2: Create Data structures.
mydb =  myclient[input('input db_name: ')]             # Create New DB
mycollection = mydb[input('input collection name: ')]  # Create New collection under the DB.

myDocuments = [{"id":1, "name":'John', "address": "Highway 37"}, #Create multiple documents for inserting
                {"id":2, "name":'Tom', "address": "Huntington 3"},
                {"id":3, "name":'Jerry', "address": "MassAve 7"},
                {"id":4, "name":'Nik', "address": "Malden 150"},
                {"id":5, "name":'Brown', "address": "Medford 2"},
                {"id":6, "name":'Zi', "address": "OneWay 9"},
                {"id":7, "name":'Brook', "address": "ParkLane 184"},
                {"id":8, "name":'Amy', "address": "Sideway 290"}]

# Step 3: Insert multiple documents to collection:
x = mycollection.insert_many(myDocuments)

# Step 5: Check all documents in this DB:
for x in mycollection.find():
    print(x)

# -----------Step 6: Check current DB name after creating:
print('Current DBs: ', myclient.list_database_names())
