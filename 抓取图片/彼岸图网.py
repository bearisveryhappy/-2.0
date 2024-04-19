# -*-codeing=utf-8-*-
# @Time : 2022/4/30 20:07
# @Author:熊金海
# @File : 彼岸图网.py
# @Software: PyCharm
import os
import requests
from bs4 import BeautifulSoup

type = int(input("请输入你要的类型[0-11]："))
page = int(input("输入页数："))
url = 'https://pic.netbian.com'
resp =requests.get(url)
resp.encoding="gbk"
soup = BeautifulSoup(resp.text,"html.parser")
classify_link = soup.find("div" ,class_="classify clearfix").find_all("a")
list = []
mz = []
for i in classify_link:
    href=i.get("href")
    name = i.text
    list.append(href)
    mz.append(name)
for i in range(1,page+1):
    if i ==1 :
        kindlink = url + list[type] + "index.html"
    else:
        kindlink= url +list[type] +f"index_{i}.html"
#def
    resp =requests.get(kindlink)
    resp.encoding="gbk"
    soup = BeautifulSoup(resp.text,"html.parser")
    photo_link = soup.find("ul" ,class_="clearfix").find_all("li")

    for i in photo_link:
        href = i.a["href"]
        inter_link = url +href
#def
        resp = requests.get(inter_link)
        resp.encoding = "gbk"
        soup = BeautifulSoup(resp.text, "html.parser")
        photo_link = soup.find("div",class_="photo-pic").find_all("a")

        for i in photo_link:
            src = i.img["src"]
            title = i.img["title"]


            filename = f"彼岸图网图片下载/{mz[type]}\\"
            if not os.path.exists(filename):
                os.makedirs(filename)

            photo_download_link=url + src
            resp = requests.get(photo_download_link)

            with open(filename+ title+".jpg",mode="wb") as f:
                f.write(resp.content)
                print(f"{title} 搞定!!!")

print("全部完成！！！")



























