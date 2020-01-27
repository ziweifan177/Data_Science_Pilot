#Python_MongoDB_Drop_db.py
from pymongo import MongoClient

myClient = MongoClient('localhost', 27017)

drop_way = input('Drop: 1-Single; 2-All: ')
if drop_way == '1':
    db_name = input('db name: ')
    mydb = myClient[db_name]

    myClient.drop_database(mydb)

if drop_way == '2':
    for db in myClient.list_database_names():
        if db != 'admin':
            myClient.drop_database(db)

print(myClient.list_database_names())
