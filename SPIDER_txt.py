import requests
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


'''
文本爬虫
'''
Useragent = UserAgent()
headers = {
    'User-Agent':Useragent.random,
}
results = requests.get("https://www.jianshu.com/p/ece967fe4342",headers = headers)
results.encoding = results.apparent_encoding
soup = BeautifulSoup(results.text)#配合BeautifulSoup获取标签内容
print(soup.find_all('section',class_="ouvJEz")[0].text)