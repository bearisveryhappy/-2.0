# -*-coding=utf-8-*-
# @Time : 2022/4/29 9:23
# @Author:熊金海
# @File : 爬取.py
# @Software: PyCharm
import requests
import os
from bs4 import BeautifulSoup


url = 'http://puwoktk.org:789/'
kind = int(input("请输入您要的类型[0-4]:"))
leaf = input("输入你要的页数：")
resp =requests.get(url)
soup =BeautifulSoup(resp.text,"html.parser")
link = soup.find('ul',class_="nav navbar-nav mr-2").find_all("a",class_="dropdown-item")
li = []
for i in link :
    href = i["href"]
    newurl =url +href
    li.append(newurl)

if leaf == 1 or leaf == 0:
    li = li[kind]
else:
    li = li[kind] +f"/{leaf}"

resp = requests.get(li)
soup = BeautifulSoup(resp.text,"html.parser")
lurl = soup.find("div",class_="list-group h6").find_all("a")

for i in lurl:
    href= i.get("href")
    name= i.text[:-10]
    newurl = url+href

    filename =f"图片/{name}\\"
    if not os.path.exists(filename):
        os.makedirs(filename)

    resp = requests.get(newurl)
    soup = BeautifulSoup(resp.text, "html.parser")
    linkurl=soup.find("div",class_="card-body h4").find_all("img",loading="lazy")

    page=0
    for i in linkurl:
        src = i["src"]
        resp = requests.get(src)
        with open(filename + str(page)+".jpg",mode="wb") as f:
            f.write(resp.content)
            page+=1
            print(f"{name}  已完成{page}张！")

print("全部搞定！！！")
