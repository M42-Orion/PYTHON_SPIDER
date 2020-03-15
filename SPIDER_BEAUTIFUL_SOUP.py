import requests
from bs4 import BeautifulSoup
'''
beautifulsoup常见的用法
'''

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
}
results = requests.get('https://s.weibo.com/user?q=蔡徐坤&Refer=weibo_user',headers = headers)
html = results.text
soup = BeautifulSoup(html)
users = soup.find('div',class_="card-wrap").find_all('div',class_ = 'card')
#
#这里有两个find，一个事find，一个事find_all，用法都相同，找到一个什么样的标签，class属性是什么
#find返回的是一个值，find_all是一个列表，所以列表需要遍历
#
#
for i in users:
    print(i.find('a',class_ = 'name').text)#名字，提取信息只需要加一个.text在后面就可以了
    print(i.find('i',class_="icon-sex")['class'][-1][9::])#性别，这里是提取class属性信息
    print(i.find('i',class_="icon-sex").parent.text[26:-18:])#所在地
    print([i.text for i in i.find('span',class_="s-nobr").parent.find_all('span')])#关注、粉丝、微博
    for i in [i.text for i in [i for i in i.find_all('p')]]:
        if i[:2:] == '简介':
            print(i)
        elif i[:2:] == '标签':
            print(i)
        elif i[:2:] == '教育':
            print(i)
        elif i[:2:] == '职业':
            print(i)
    print('————————————————————————————————————————————————————————————————————————————————————————————————')