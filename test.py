import requests
from bs4 import BeautifulSoup
'''
beautifulsoup常见的用法
'''

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
}
results = requests.get('https://www.taptap.com/top/download',headers = headers)
html = results.text
soup = BeautifulSoup(html)

for i in soup.find_all('div',class_="taptap-top-card"):
    print(i.find('span',class_ ="top-card-order-text").string)
# print(soup.find_all('div',class_="taptap-top-card")[0].find_all("span",class_ = "top-card-order-text orange"))

# import requests
# from bs4 import BeautifulSoup
# import random
# from multiprocessing import Pool
# def Request(i_d):
#     url = "http://www.yft166.net/ParkingPayment/ComputeParkingFee?licensePlate=%E8%8B%8FE0{}EV8&parkingId=".format(i_d)

#     payload = {}
#     headers = {
#         'Host': 'www.yft166.net',
#         'Proxy-Connection': 'keep-alive',
#         'Cache-Control': 'max-age=0',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64)AppleWebKit/537.36 (KHTM',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Referer': 'http://www.yft166.net/ParkingPayment/LicensePlatePayment?menuEnter=True',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
#         'Cookie': 'ASP.NET_SessionId=ialilvff5mk22er5sbhv3ef1; SmartSystem_WeiXinOpenId=oussCwPQEcfA4uLaI_PwCKBc0Ohc; SmartSystem_WeiXinUser_DefaultPlate=%e8%8b%8fE'
#     }

#     response = requests.request("GET", url, headers=headers, data=payload)
#     soup = BeautifulSoup(response.text,features="lxml")
#     a = response.cookies
#     # print(response.cookies)
#     # print(soup)


#     print(soup.find_all("div",class_ = "header_change")[0].text)
#     # print(response.text)

# # for i in range(100):
# #     try:
# #         i_d = random.randint(1,9)
# #         Request(i_d)
# #         print("成功:",i)
# #     except :
# #         print(i)

# def mian():
#     # a = []
#     # for i in range():
#     #     a.append(random.randint(1,9))
#     pool = Pool()#创建进程池
#     pool.map(Request,[1,2,3,4,5,6,7,8])
#     pool.close() # 将进程池关闭，不再接受新的进程
#     pool.join() # 主进程阻塞，只有池中所有进程都完毕了才会通过

# mian()
