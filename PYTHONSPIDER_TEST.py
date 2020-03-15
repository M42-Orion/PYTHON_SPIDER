import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

Useragent = UserAgent()
headers = {
    'User-Agent':Useragent.random,
}

results = requests.get('https://www.baidu.com/',headers=headers)#get方式请求该网址
results.encoding = results.apparent_encoding#获取网页编码，对网页内容进行编码，防止乱码产生
# results_json = json.loads(results.text)
print(results.text)#查看返回结果
soup = BeautifulSoup(results.text)#配合BeautifulSoup获取标签内容
print(soup.title.text)
