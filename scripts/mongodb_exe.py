import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient ['mydatabase']

#check if a mongodb exists in your system
dblist = myclient.list_database_names()
if "mynewdatabase" in dblist:
    print("The database exists");

##print all the mongodb in your system
##print(myclient.list_database_names());
#
#
###create collection ___ similar to table in RDBMS
##collection_name = customers
#    
########## create operation #################
#    
## Hierarchy _____ database - collection(table) - document(record)
#mycol = mydb["customers"]
#mydict1 = {"name":"arjun", "address":"chandrapur"}
#x = mycol.insert_one(mydict1);
#mydict2={"name":"bhim","address":"uttarpradesh"}
#x = mycol.insert_one(mydict2)
#print(x.inserted_id); #prints unique id given to the document by mongodb database
#
#mylist1 = [
#        {"name":"anish","address":"butwal"},
#        {"name":"krinjwal","address":"hetauda"},
#        {"name":"narayan","address":"hetauda"}
#        ]
#
#x = mycol.insert_many(mylist1)
#
#mylist2 = [
#        {"name":"vladimir","address":"russia","street":"kgb_avenue"}, 
#        {"name":"donald trump","address":"donald_building"}  # id explicitely put as "_id":1 ;      
#        ]
#x = mycol.insert_many(mylist2);
#
#print(x.inserted_ids)
#
#####################################
## select in mysql === findone, find in mongodb
#y = mycol.find_one() ## if id's have been explicitely defined above it causes bulkwriteerror
#print(y)
#
#print("##############################");
#for x in mycol.find({},{"name":1,"address":1}):
#    print (x)
##cannot have name = 1 and address = 0 at same time,to supress a field don't include it or give 0 value to it woithout specifying other fileds
## include "_id":0 field in order to see name and address returned, it supresses ObjectId field
#
#for x in mycol.find({},{"address":0}):
#    print (x)
#
#print("finding the values:")
#### filter the result accourding to value of key
#myquery1 = {"address":"hetauda"}
#mydoc = mycol.find(myquery1)
#for x in mydoc:
#    print(x)
#    
#print("*********** using gt, lt ********")
### gt : greater than or equals to 
### lt : only less than
#myquery1 = {"address": {"$lt":"d"}}
#mydoc = mycol.find(myquery1)
#for h in mydoc:
#    print(h);
#    
#print("%%%%%%%%%%%%% using regex to catch values name starting with %%%%%%%%%%%%");
#myquery2 = {"address":{"$regex": "^b"}}
#mydoc = mycol.find(myquery2);
#
#for u in mydoc:
#    print(u)
#    
##### sorting ########
## sort takes two params:
## 1st parameter: field name
## 2nd parameter: representation of sort in asc(1) or desc(-1)
#
#print("******************************* sorting starts here *************************")
#mg1 = mycol.find().sort("name", -1)
#for o in mg1:
#    print(o)
#    
##################### delete document (row) #####################################
#
#mg2 = {"address":"hetauda"};
#
#k = mycol.delete_many(mg2);
#
#print("trying to find instances of ** hetauda ** after deleting all documents with address** hetauda **")
### use delete_many(mg2) method to delete all instances of mg2
#myquery3 = {"address":{"$regex":"^h"}}
#mg3 = mycol.find(myquery3);

#for h in mg3:
#    print(h)
    
## for deleting documents with address starting with particular letter, write a query to match "key with those letters"
## then apply collection_name.delete_many(query matching the starting letter)

#print(k.deleted_count, "documents deleted")


### to delete all documents #####

# chett = mycol.delete_many({})
# print(chett.deleted_count,"documents deleted")

## delete collection ###
#mycol.drop()


mycolp = mydb["phone_Book"]
yatch = mycolp.delete_many({});
print(yatch.deleted_count,"documents deleted");
mydict1 = [
        {"name":"arjun", "address":"Rautahat"},
        {"name":"usha","address":"ushapur"}
        ]
h = mycolp.insert_many(mydict1)

myquery = {"address":"Rautahat"}
newvalue = {"$set":{"address":"Durgachowk"}}


y = mycolp.update_many(myquery,newvalue)

##use update_many to apply newvalue to all queries

print(y.modified_count,"documents updated")
for x in mycolp.find():
    print (x)
    

############ limiting the result in mongodb ##############
### use limit command here

print("\n the value shown after limiting: \n")
for x in mycolp.find().limit(1):
    print (x)
    