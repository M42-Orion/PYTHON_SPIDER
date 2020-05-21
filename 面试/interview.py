import requests
from bs4 import BeautifulSoup
import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Interview"]
download = mydb["download"]
new = mydb["new"]
reserve = mydb["reserve"]
sell = mydb["sell"]
played = mydb["played"]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
}
game_tags = ['download','new','reserve','sell','played']

def request(game_tag):
    results = requests.get('https://www.taptap.com/top/{}'.format(game_tag),headers = headers)
    return BeautifulSoup(results.text)

def request_ajax(game_tag,page):
    results = requests.get('https://www.taptap.com/ajax/top/played?page=2&total=30',headers = headers)
    results.encoding = results.apparent_encoding#获取网页编码，对网页内容进行编码，防止乱码产生
    results_json = json.loads(results.text)
    return BeautifulSoup(results_json['data']['html'])

def save(soup,game_tag):
    for i in soup.find_all('div',class_="taptap-top-card"):
        Ranking =  i.find('span',class_ = "top-card-order-text").string
        title = i.find('a',class_ = "card-middle-title").h4.string
        author = i.find('p',class_ = "card-middle-author").a.string
        rating = i.find('p',class_ = "middle-footer-rating").span.string
        description = i.find('p',class_ = "card-middle-description").string
        tags = [i.string for i in i.find('div',class_ = "card-tags").find_all("a")]
        category = i.find('div',class_ = "card-middle-category").a.string
        mydict = {
                "Ranking": Ranking,
                "title": title,
                "author": author,
                "rating":rating,
                "description":description,
                "tags":str(tags),
                "category":category
                }
        eval("{}.insert_one(mydict)".format(game_tag))

if __name__ == '__main__':
    for game_tag in game_tags:
        soup = request(game_tag)
        save(soup,game_tag)
        for page in range(2,10):
            soup = request_ajax(game_tag,page)
            save(soup,game_tag)