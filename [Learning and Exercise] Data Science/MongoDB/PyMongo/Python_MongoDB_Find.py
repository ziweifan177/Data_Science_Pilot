# Python_MongoDB_Find.py

from pymongo import MongoClient

# Step 1: Connect to db>collections
myclient = MongoClient('localhost', 27017)
print('Current DBs of Creating session: ', myclient.list_database_names())

db_name = input('input db name: ')
mydb = myclient[db_name]
mycollection = mydb['demo_collection']

# Step 2: Fetch
method = input('input method: 1-find_one; 2-fetch all; 3-find by key; 4-find by Regular expression; 5-Sort Ascend; 6-Sort Descend;')
if method == '1': # 1-find_one
    x = mycollection.find_one() # Get a single document from the database.
    print('find one: ', x) # {'_id': ObjectId('5e2df8ca701e9e7812634206'), 'id': 1, 'name': 'John', 'address': 'Highway 37'}

elif method == '2': # 2-fetch all
    for x in mycollection.find(): # Get all documents under this collection.
        print(x)

elif method == '3': # 3-find by key;
    query = {'name':'John'}  # Get all documents of names equals to 'John'
    for x in mycollection.find(query):
        print(x)

elif method == '4': # 4-Regular Expression
    query = {'name':{"$regex": "^J"}} # Get all documents of names started with 'J'
    for x in mycollection.find(query):
        print(x)

elif method == '5': # 5- Sort Ascend;
    mydocs = mycollection.find().sort('name', 1) # 1: Ascend
    for x in mydocs:
        print(x)

elif method == '6': # 6- Sort Descend;
    query = {'name': {"$regex": '^J'}}
    mydocs = mycollection.find(query).sort('name', -1) # -1: Name of 'J' + Descend
    for x in mydocs:
        print(x)

print('Current DBs: ', myclient.list_database_names())
