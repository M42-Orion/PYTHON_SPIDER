import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ippool"]
mycol = mydb["sixsixip"]

# for i in mycol.find({"ipadd":'109.248.62.207'}):
#     print(bool(i))

# mycol.insert_one({"ipadd":"103.42.162.30" ,"port":"8080"})
# 103.42.162.30 8080
# print(bool(mycol.find({"ipadd":'10.248.62.207'})))
# mycol.update({"ipadd":"41.254.46.154" ,"port":"9999"},{'$setOnInsert': {"ipadd":"41.254.46.154" ,"port":"9999"}},upsert=True)
# print(type([i for i in mycol.find()][2]))
import random

List=[{1},{2},{3},{4},{5}]

print(random.sample(List,1))