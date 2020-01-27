# Python_MongoDB_Delete.py

from pymongo import MongoClient

myClient = MongoClient('localhost', 27017)
print('Current DBs of Deleting session: ', myClient.list_database_names())

db_name = input('DB name:')
mydb = myClient[db_name]
mycollection = mydb['demo_collection']

delete_way = input('Delete by: 1-single; 2-multiple')
if delete_way == '1':
    query = {'name': 'John'}
    deletedX = mycollection.delete_one(query) # Delete 1st document with name 'John'

    for x in mycollection.find():
        print(x)

elif delete_way == '2': # Delete multiple documents with name started with 'Z'
    query = {'name': {'$regex': '^Z'}}
    deletedX = mycollection.delete_many(query)

    for x in mycollection.find():
        print(x)
