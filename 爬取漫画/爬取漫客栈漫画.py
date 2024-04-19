# -*-codeing=utf-8-*-
# @Time : 2022/4/28 11:02
# @Author:熊金海
# @File : 爬取我的师兄实在是太稳了漫画.py
# @Software: PyCharm
import requests
import json
import os
from bs4 import BeautifulSoup

name = input("您要搜索的关键字：")

# file = f'{name}\\'
# if not os.path.exists(file):
#     os.mkdir(file)

url = f'https://www.mkzhan.com/search/?keyword={name}'
head_first_url = url.split("/search")[0]

resp = requests.get(url)
content = resp.text
soup = BeautifulSoup(content,"lxml")
li = soup.find("p", class_="comic__title")
href = li.a["href"]
url_up = head_first_url +href


resp =requests.get(url_up)
soup = BeautifulSoup(resp.text,"lxml")
li2 = soup.find("ul", class_="chapter__list-box clearfix hide").find_all("li")
for n in li2:
    hreflink =n.a["data-hreflink"]
    name = n.a.text
    name =name.strip()
    id1 = hreflink[8:-5]
    id2 = hreflink[1:-12]
    cartoon = f"https://comic.mkzcdn.com/chapter/content/v1/?chapter_id={id1}&comic_id={id2}&format=1&quality=1&type=1"

    filename = f'{name}\\'
    if not os.path.exists(filename):
        os.mkdir(filename)
#
    resp_up = requests.get(cartoon).json()
    image = resp_up["data"]["page"]
    page =0
    for n in image:
        name = n["image"]
        # print(name)

        resp=requests.get(name)
        # print(image)
        with open(filename + str(page)+".jpg",mode="wb") as f:
            f.write(resp.content)
            print(f"{filename}下载第{page}页")
            page+=1
print("全部搞定！！！")








