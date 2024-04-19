# -*-codeing=utf-8-*-
# @Time : 2022/3/27 13:52
# @Author:???
# @File : 爬取新发地网页+保存.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import csv
import io
import sys


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
url ='http://www.xinfadi.com.cn/index.html'

resp=requests.get(url)
resp.encoding="utf-8"
f=open("菜价.csv",mode="w")

csvwriter=csv.writer(f)

page=BeautifulSoup(resp.text,"html.parser")

tbody=page.find("tbody",class_="ul")

trs=tbody.find_all("tr")[1:]

for tr in trs:
    tds=tr.find_all("td")
    name =tds[0].text
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    place = tds[6].text
    date = tds[7].text
    csvwriter.writerow([name,low,avg,high,gui,kind,place,date])
    f.close()
print("over~!!")

