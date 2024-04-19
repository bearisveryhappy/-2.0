# -*-codeing=utf-8-*-
# @Time : 2023/1/31 20:29
# @Author:熊金海
# @File : 小说.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import os
import re
import time

def main(url):
    carkoon = f'/ebb1/list/{page}/{leaf}'
    baseurl = url + carkoon
    resp2 = requests.get(baseurl)
    soup2 = BeautifulSoup(resp2.text,"html.parser")
    list2 = soup2.find("div", class_="list-group h6").find_all('a')
    usr(list2,url)
def usr(list2,url):
    page = 0
    for i in list2:
        href2 = i.get("href")#href2 = /ebb1/show/tdwxdf
        name = i.text
        img_name = name[:-10]

        filename = f'{img_name}\\'
        if not os.path.exists(filename):
            os.mkdir(filename)

        baseurl2 = url + href2
        resp3 = requests.get(baseurl2)
        soup3 = BeautifulSoup(resp3.text, "lxml")
        item = soup3.find("div", class_="card-body h4", id="content")

        content = item.text
        text_2 = re.sub("\n", "", content)
        text_1 = re.sub("　　", "\n", text_2).strip()

        f = open(filename + img_name +".txt", mode='w')
        f.write(text_1)
        print("over!!", page)
        page += 1

if __name__ == '__main__':
    page = input("请输入您要的类型[14-18]：")
    leaf = int(input("输入你想要的页数： "))
    url = 'http://ddnnpap.com'
    main(url)