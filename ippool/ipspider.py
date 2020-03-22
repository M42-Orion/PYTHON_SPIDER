import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pymongo
from multiprocessing import Pool


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ippool"]
mycol = mydb["sixsixip"]

Useragent = UserAgent()
headers = {
    'User-Agent':Useragent.random,
}

def iptest(ipadd,port):
    url = 'https://www.baidu.com/'
    try:
        response = requests.get(url,headers=headers,proxies={ "https": "http://{}:{}".format(ipadd,port)},timeout = 10 )# 使用代理
        # print(response.status_code)
        if response.status_code == 200:
            print("有效代理",ipadd,port)
            mycol.update({"ipadd":ipadd ,"port":port},{'$setOnInsert': {"ipadd":ipadd ,"port":port}},upsert=True)
            #有则存，没有则跳过
    except:
        print("失败")

def scrapy(url):
    results = requests.get(url,headers=headers)
    results.encoding = results.apparent_encoding#获取网页编码，对网页内容进行编码，防止乱码产生
    soup = BeautifulSoup(results.text,features="lxml")#配合BeautifulSoup获取标签内容
    ip_list = soup.find_all('table')[2].find_all('tr')
    for ip in ip_list:
        List = ip.find_all('td')
        iptest(List[0].string,List[1].string)

def mian():
    pool = Pool()#创建进程池
    pool.map(scrapy,['http://www.66ip.cn/{}.html'.format(i) for i in range(1,20)])
    pool.close() # 将进程池关闭，不再接受新的进程
    pool.join() # 主进程阻塞，只有池中所有进程都完毕了才会通过

# if __name__ == "__main__":
#     main()
