#https://c-ssl.duitang.com/uploads/item/202001/19/20200119142316_euaol.jpg
import requests
from bs4 import BeautifulSoup
import os


'''
图片爬虫
'''
try:
    os.mkdir("image")
except:
    pass

results = requests.get('https://c-ssl.duitang.com/uploads/item/202001/19/20200119142316_euaol.jpg')#get方式请求该网址

with open('image/诸葛大力.jpg', 'wb') as f:
            f.write(results.content)
            f.close()
            print("文件保存成功")