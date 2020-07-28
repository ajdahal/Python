import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['database_X']

dblist = myclient.list_database_names();

if "database_X" in dblist:
    print("The database exists");
    
    
mycol = mydb["customers"]
xyz = {"name" : "arjun", "address" : "chandrapur"};
x = mycol.insert_one(xyz);
print(x.inserted_id)

y = mycol.find_one();
print(y)

for u in mycol.find({},{"address":1}):
    print(u)
    
myquery1 = {"address": {"$gt":"^c"}}
myquery2 = {"$set":{"address":"durgachowk"}}
y = mycol.update_many(myquery1,myquery2);
for h in mycol.find():
    print(h)
myx = mycol.find().sort("name",1);
for r in myx:
    print (r);

k = mycol.delete_many(myquery1)
mycol.drop()