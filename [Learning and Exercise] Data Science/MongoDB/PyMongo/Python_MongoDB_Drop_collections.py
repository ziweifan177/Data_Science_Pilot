# Python_MongoDB_Drop_collections.py
from pymongo import MongoClient

myClient = MongoClient('localhost', 27017)
print(myClient.list_database_names())

db_name = input('input db name: ')
mydb = myClient[db_name]

print(mydb.list_collection_names())
collection_name = input('collection name to drop: ')

myCollection = mydb[collection_name]
myCollection.drop() # Drop collection
