import requests
from fake_useragent import UserAgent
from lxml import etree


'''
Xpath基本使用
'''

Useragent = UserAgent()
headers = {
    'User-Agent':Useragent.random,
}

results = requests.get(r'https://s.weibo.com/weibo?q=%E6%B2%88%E4%BB%8E%E6%96%87&Refer=index',headers=headers)#get方式请求该网址
# results.encoding = results.apparent_encoding#获取网页编码，对网页内容进行编码，防止乱码产生
# print(results.text)#查看返回结果
html = etree.HTML(results.text)
All = html.xpath('/html/body/div[1]/div[2]/ul/li[1]/a/text()')
people = html.xpath('/html/body/div[1]/div[2]/ul/li[2]/a/text()')
essay = html.xpath('/html/body/div[1]/div[2]/ul/li[3]/a/text()')
print(All,people,essay)

