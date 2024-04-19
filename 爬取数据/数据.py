# -*-codeing=utf-8-*-
# @Time : 2022/3/6 10:00
# @Author:熊金海
# @File : 猎聘爬取.py
# @Software: PyCharm
import csv
import io
import re
import sys

import requests
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
url = 'https://www.tiobe.com/tiobe-index/'



resp = requests.get(url,)
resp.encoding="utf-8"

f= open("../数据.json", mode='w')
csvwriter=csv.writer(f)
content=resp.text
findR=re.compile(r'<td.*?>(.*?)</td>',re.S)
# findS=re.compile(r'<td _msthash="" _msttexthash="">(.*?)</td>',re.S)
# findT=re.compile(r'<td _msthash="" _msttexthash="">(.*?)</td>',re.S)
# findF=re.compile(r'<td _msthash="" _msttexthash="">(.*?)</td>',re.S)
# findN=re.compile(r'<td _msthash="" _msttexthash="">(.*?)</td>',re.S)

soup = BeautifulSoup(content,"html.parser")
for item in soup.find("tbody").find_all("tr"):
    item=str(item)

    replace=re.findall(findR,item)
    # salary=re.findall(findS,item)
    # company=re.findall(findT,item)
    # fuli = re.findall(findF,item)
    # name=re.findall(findN,item)
    dict=(replace)

    csvwriter.writerow(dict)
    print("爬取完毕！！！")


