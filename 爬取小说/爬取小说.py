# -*-codeing=utf-8-*-
# @Time : 2022/4/28 21:54
# @Author:熊金海
# @File : 爬取小说.py
# @Software: PyCharm
import requests
import os
import re
import time
from bs4 import BeautifulSoup

page = input("请输入您要的页类型[14-18]：")
url = 'http://puwoktk.org:789'
carkoon =f'/enbb1/list/{page}'
baseurl =url +carkoon

resp2 = requests.get(baseurl)
soup2 = BeautifulSoup(resp2.text,"html.parser")
list2 = soup2.find("div",class_="list-group h6").find_all('a')


for i in list2 :
    href2 =i.get("href")
    name = i.text
    img_name=name[:-10]

    filename=f'{img_name}\\'
    if not os.path.exists(filename):
        os.mkdir(filename)


    baseurl2 =url +href2
    resp3 =requests.get(baseurl2)
    soup3 =BeautifulSoup(resp3.text,"html.parser")
    item = soup3.find("div",class_="card-body h4",id="content")

    content = item.text
    text_2 = re.sub("\n", "", content)
    text_1 =re.sub("　　","\n",text_2).strip()

    page =0
    f = open(filename + img_name , mode='w')
    f.write(text_1)
    for i in range(1,page):
        print("over!!", page)
        page+=1

print("all over!!!")

