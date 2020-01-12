import requests
import json
from fake_useragent import UserAgent

Useragent = UserAgent()
headers = {
    'User-Agent':Useragent.random,
}
start,_,status = 24,1578817942960,True

def page(url):#给定一个url，返回当前页面的所有图片链接
    try:
        response = requests.get(url,headers = headers)
        return [i['photo']['path'] for i in json.loads(response.text)['data']['object_list']]
    except:
        return []

def page_save(url_image,K):#文件写入
    response = requests.get(url_image)
    with open("{}.jpeg".format(K), "wb") as fp:
        for data in response.iter_content(128):
            fp.write(data)
    print("第{}副图保存成功".format(K))

def main(start,_,status):
    K = 0
    while status == True:
        url = "https://www.duitang.com/napi/blog/list/by_album/?album_id=83959491&limit=24&include_fields=top_comments%2Cis_root%2Csource_link%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Creply_count&start={}&_={}".format(start,_)
        List_image = page(url)
        start = start + 24
        _ = _ + 1
        if len(List_image) == 0:
            status = False
            print(start,_)
        else:
            for i in List_image:
                page_save(i,K)
                K = K + 1

if __name__ =='__main__':
     main(start,_,status)