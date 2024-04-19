# -*-codeing=utf-8-*-
# @Time : 2022/4/19 12:13
# @Author:熊金海
# @File : 梨视频爬取.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
url ='https://www.pearvideo.com/video_1759502'
head ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
    'Referer': url
}

contID=url.split("_")[1]
videourl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.21561641050056646'
resp = requests.get(videourl,headers=head)
dic = resp.json()

srcURl= dic['videoInfo']['videos']['srcUrl']
systemTime =dic['systemTime']
srcURl=srcURl.replace(systemTime,f'cont-{contID}')

with open(f"{contID}.mp4","wb") as f:
    f.write(requests.get(srcURl).content)

print("爬取完毕！！")















