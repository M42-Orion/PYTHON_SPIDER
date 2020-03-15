import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
from multiprocessing import Pool
import time


'''
多进程爬虫，pool进程池
'''
Useragent = UserAgent()
headers = {
    'User-Agent':Useragent.random,
}
def request(n):
    results = requests.get('https://movie.douban.com/subject/26266893/comments?start={}&limit=20&sort=time&status=P&comments_only=1'.format(n),headers=headers)#get方式请求该网址
    results.encoding = results.apparent_encoding#获取网页编码，对网页内容进行编码，防止乱码产生
    results_json = json.loads(results.text)
    soup = BeautifulSoup(results_json['html'])#配合BeautifulSoup获取标签内容
    for i in soup.find_all('div',class_ = 'comment'):
        name = i.find('span',class_ = 'comment-info').a.string
        fraction = i.find('span',class_ = 'comment-info').find_all('span')[1]['title']
        comment = i.p.span.string
        print(n,':',name,fraction,comment,'\n')


if __name__ == "__main__":
    start_time=time.time()  #开始时间
    pool = Pool()#创建进程池
    pool.map(request,[i*20 for i in range(10)])
    pool.close() # 将进程池关闭，不再接受新的进程
    pool.join() # 主进程阻塞，只有池中所有进程都完毕了才会通过
    end_time=time.time()   #结束时间
    print("time:%d"  % (end_time-start_time))  #结束时间-开始时间 2s

    # start_time=time.time()  #开始时间
    # for i in range(10):
    #     request(i*20)
    # end_time=time.time()   #结束时间
    # print("time:%d"  % (end_time-start_time))  #结束时间-开始时间 8s
