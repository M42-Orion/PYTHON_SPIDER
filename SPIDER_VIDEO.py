#http://video.dispatch.tc.qq.com/uwMROfz2r5xgoaQXGdGnDGdfKYBirXlD0BbRlP-fWS3CoV5R/r0033saj8tr.p212.2.mp4?sdtfrom=v1001&type=mp4&start=26&vkey=B84B9578A52EA29AAD07029EC00825BAA3887A45B3FBB4E5E6344605576CFE3334A7E1487EAA933A1B62BCB1C793EF29AF7A65482290BE815B14EAF4973B93396A1A291DD7F835BA10E68178B694D031E31F8E28D97D850818500FB4F422CF66C07ADF905653FDCA217E18D8DDB7141905C19563152741EEA1D87CC8E7862343ECB042E282558E8F&level=0&platform=70202&br=125&fmt=hd&sp=0&guid=095754CFD63856889F822132192D623B6C869A9D
import requests
from bs4 import BeautifulSoup
import os


'''
视频爬虫
'''
try:
    os.mkdir("video")
except:
    pass

results = requests.get('http://video.dispatch.tc.qq.com/uwMROfz2r5xgoaQXGdGnDGdfKYBirXlD0BbRlP-fWS3CoV5R/r0033saj8tr.p212.2.mp4?sdtfrom=v1001&type=mp4&start=26&vkey=B84B9578A52EA29AAD07029EC00825BAA3887A45B3FBB4E5E6344605576CFE3334A7E1487EAA933A1B62BCB1C793EF29AF7A65482290BE815B14EAF4973B93396A1A291DD7F835BA10E68178B694D031E31F8E28D97D850818500FB4F422CF66C07ADF905653FDCA217E18D8DDB7141905C19563152741EEA1D87CC8E7862343ECB042E282558E8F&level=0&platform=70202&br=125&fmt=hd&sp=0&guid=095754CFD63856889F822132192D623B6C869A9D')#get方式请求该网址

with open('video/斗罗大陆.ts', 'wb') as f:
            f.write(results.content)
            f.close()
            print("文件保存成功")