import pymongo
import pymongo
from urllib import parse

'''
操作mongodb
'''
# 转义用户名和密码
user = parse.quote_plus("dbuser")
passwd = parse.quote_plus("MongoDBmima12!")
# client = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0-vf6jv.mongodb.net/test?retryWrites=true&w=majority".format(user,passwd))
client = pymongo.MongoClient("mongodb+srv://dbuser:{}@xiaobai-vf6jv.gcp.mongodb.net/test?retryWrites=true&w=majority".format(passwd))

db = client.test2
mycol = db["table"]

#增
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
mycol.insert_one(mydict) 

mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
mycol.insert_many(mylist)
#删
myquery = { "name": "Taobao" } 
mycol.delete_one(myquery)
#查
for x in mycol.find({},{"name": "Taobao"}):
  print(x)