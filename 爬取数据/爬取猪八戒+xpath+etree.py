# -*-codeing=utf-8-*-
# @Time : 2022/3/29 17:15
# @Author:熊金海
# @File : 爬取猪八戒+xpath+etree.py
# @Software: PyCharm

import requests
from lxml import etree
import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
i = input("请输入你想搜索的职业：")
url = f'https://nanchang.zbj.com/search/f/?kw={i}'

resp = requests.get(url)
resp.encoding="utf-8"
f=  open("猪八戒.csv",mode="w")
csvwriter=csv.writer(f)
html = etree.HTML(resp.text)  #解析

divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div/div')
for div in divs :
    price= div.xpath('./div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip("?")
    title= "i".join(div.xpath('./div/a[2]/div[2]/div[2]/p/text()'))
    name= div.xpath('./div/a[1]/div[1]/p/text()')[1].strip("\n")
    location= div.xpath('./div/a[1]/div[1]/div/span/text()')[0]
    csvwriter.writerow([title,name,location,price])
print("over!!!")













