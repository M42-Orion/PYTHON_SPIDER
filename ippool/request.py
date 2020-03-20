import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pymongo

Useragent = UserAgent()
headers = {
    'User-Agent':Useragent.random,
}
def iptest(ipadd,port):
    url = 'https://www.baidu.com/'
    try:
        response = requests.get(url,headers=headers,proxies={ "http": "http://{}:{}".format(ipadd,port)}) # 使用代理
        # print(response.status_code)
        if response.status_code == 200:
            print("有效代理")
    except requests.ConnectionError as e:
        print(e.args)

def scrapy(url):
    results = requests.get(url,headers=headers)
    results.encoding = results.apparent_encoding#获取网页编码，对网页内容进行编码，防止乱码产生
    soup = BeautifulSoup(results.text)#配合BeautifulSoup获取标签内容
    ip_list = soup.find_all('table')[2].find_all('tr')
    for ip in ip_list:
        List = ip.find_all('td')
        iptest(List[0].string,List[1].string)

scrapy('http://www.66ip.cn/3.html')

# results = requests.get('https://www.baidu.com/',headers=headers)#get方式请求该网址
# results.encoding = results.apparent_encoding#获取网页编码，对网页内容进行编码，防止乱码产生
# # results_json = json.loads(results.text)
# print(results.text)#查看返回结果
# soup = BeautifulSoup(results.text)#配合BeautifulSoup获取标签内容
# print(soup.title.text)
