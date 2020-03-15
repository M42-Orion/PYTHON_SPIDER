from multiprocessing import Pool
import requests
from requests.exceptions import ConnectionError

'''
map
'''

def scrape(url):
    # try:
    #     print(requests.get(url))
    # except ConnectionError:
    #     print('Error',url)
    # finally:
    #     print('URL',url,'Scraped')
    print(requests.get(url))

if __name__ == "__main__":
    pool = Pool(processes=3)
    urls = [
        'https://www.baidu.com/',
        'http://www.meituan.com'
        'http://blog.csdn.net/'
    ]
    pool.map(scrape,urls)