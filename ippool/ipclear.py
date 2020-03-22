import pymongo
import requests
from fake_useragent import UserAgent

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ippool"]
mycol = mydb["sixsixip"]
Useragent = UserAgent()
headers = {
    'User-Agent':Useragent.random,
}

def ip_clear(ipadd,port):
    try:
        url = 'https://www.baidu.com/'
        response = requests.get(url,headers=headers,proxies={ "https": "http://{}:{}".format(ipadd,port)},timeout = 10 )# 使用代理
        # print(response.status_code)
        if response.status_code == 200:
            print("有效代理",ipadd,port)
            #有则存，没有则跳过
    except:
        mycol.delete_one({"ipadd":ipadd ,"port":port})
        print({"ipadd":ipadd ,"port":port})
    

def main():
    for i in mycol.find():
        ip_clear(i['ipadd'],i['port'])

main()