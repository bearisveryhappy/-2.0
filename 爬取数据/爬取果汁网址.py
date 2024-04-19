# -*-codeing=utf-8-*-
# @Time : 2022/4/27 18:18
# @Author:熊金海
# @File : 爬取果汁网址.py
# @Software: PyCharm
import re
import os
import requests
import csv
from bs4 import BeautifulSoup
import json

url = 'http://www.guozhivip.com/'

findoften=re.compile(r'.*?href="(.*?)".*?',re.S)
findname=re.compile(r'<a.*>(.*?)</a>')


resp = requests.get(url)
content = resp.text

li = []
soup =BeautifulSoup(content,"lxml")
for item in soup.find("div" ,class_="row row-cols-1 row-cols-sm-1 row-cols-md-2 row-cols-lg-3").find_all("a"):
    item =str(item)

    url =re.findall(findoften,item)[0]
    li.append(url)

    name =re.findall(findname,item)[0]
    li.append(name)

    f = open("爬取果汁网址.csv","w")
    csvwriter=csv.writer(f)
    print(li)
    # for i in li:
    #     print(i)
        # csvwriter.writerow(i)

print("搞定！！！")








