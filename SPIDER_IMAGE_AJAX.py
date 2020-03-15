#https://huaban.com/search/?q=%E8%AF%B8%E8%91%9B%E5%A4%A7%E5%8A%9B&k77hfl6o&page=2&per_page=20&wfl=1
# https://hbimg.huabanimg.com/49c2a8afb7fcf65fe1d08209ea80b9c85e603c6990cb-fdazbg
import requests
from bs4 import BeautifulSoup
import os
import json

'''
ajax花瓣网图片爬虫
'''
try:
    os.mkdir("image")
except:
    pass

def ajax(n):
    results = requests.get(r'https://api.huaban.com/search/?q=%E8%AF%B8%E8%91%9B%E5%A4%A7%E5%8A%9B&k77hfl6o&page={}&per_page=20&wfl=1'.format(n))#get方式请求该网址
    results.encoding = results.apparent_encoding
    results_json = json.loads(results.text)
    for i in results_json['pins']:
        # print(i['pin_id'])#图片id
        # print(i['file']['key'])#图片地址
        with open('image/{}.jpg'.format(i['pin_id']), 'wb') as f:
            results = requests.get(r'https://hbimg.huabanimg.com/'+i['file']['key'])#图片真实地址
            f.write(results.content)
            f.close()
            print(i['pin_id'],"文件保存成功")

if __name__ == "__main__":
    for i in range(1,5):
        try:
            ajax(n)
        except:
            pass