# Python_MongoDB_Update.py

from pymongo import MongoClient

myClient = MongoClient('localhost', 27017)
db_name = input('db_name: ')

mydb = myClient[db_name]
myCollection = mydb['demo_collection']

update_way = input('Update by: 1-single; 2-multiple')

if update_way=='1':
    query = {'name': 'Nik'}
    newValue = {'$set': {'name': 'Nik22222'}}

    myCollection.update_one(query, newValue) # Single Update

elif update_way == '2':
    query = {'name': 'Amy'}
    newValues = {'$set': {'name': 'Amy22222'}}

    myCollection.update_many(query, newValues) # multiple update

for x in myCollection.find().limit(8): # Display the top N
    print(x)
