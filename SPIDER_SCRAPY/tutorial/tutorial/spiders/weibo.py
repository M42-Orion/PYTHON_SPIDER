# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['s.weibo.com']
    start_urls = ['https://s.weibo.com/weibo/%25E5%25B2%25B3%25E4%25BA%2591%25E9%25B9%258F?topnav=1&wvr=6']

                    
    # 重载start_requests方法
    def start_requests(self):
        url = 'https://s.weibo.com/user?q=%E5%B2%B3%E4%BA%91%E9%B9%8F&Refer=weibo_user'
        headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
        # 指定cookies
        cookies = {
            'MLOGIN': '1', 
            'WEIBOCN_FROM': '1110006030', 
            'SCF': 'Art5xhYEloxGpUp_gy0CrNMb39zsZpmvPKFDk3O7TwWj-9gseA5BGJay3NJHhBR0ajxurXNIaTSpkxwX6HWOP9E.', 
            '_T_WM': '26723672006', 
            'SSOLoginState': '1583609025', 
            'M_WEIBOCN_PARAMS': 'uicode%3D20000174', 
            'XSRF-TOKEN': 'a88288', 
            'SUHB': '08JrogEnY36tjx', 
            'SUB': '_2A25zZ4SRDeRhGeBG7FUV9ifPzT2IHXVQqyzZrDV6PUJbkdAKLWjhkW1NQeFDpIhkzgWQekAYw2p2d7DA9x9ywS4B'}
 
                # 再次请求到详情页，并且声明回调函数callback，dont_filter=True 不进行域名过滤，meta给回调函数传递数据
        yield scrapy.Request(url=url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        user = response.css('.info .name')
        # print(user)
        for i in user:
            selector = Selector(text = i.extract())
            print('_'.join(selector.xpath("//text()").extract()))
        # print(response.css('.m-page .next a::attr("href")').extract())
        # print(response.css('.next::attr("href")').extract())
        url = response.urljoin(response.css('.next::attr("href")').extract()[0])
        print(url)
        yield scrapy.Request(url=url, callback=self.parse)
