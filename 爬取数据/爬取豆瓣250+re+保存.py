# -*-codeing=utf-8-*-
# @Time : 2022/3/27 10:36
# @Author:熊金海
# @File : 爬取豆瓣250+re+保存.py
# @Software: PyCharm
import re
import requests
import csv

url='https://movie.douban.com/top250'

header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"
}
resp=requests.get(url=url,headers=header)
resp.encoding="gbk"
content=resp.text

obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
               r'.*?<span class="other">&nbsp;/&nbsp;(?P<rename>.*?)</span>'
               r'.*?<p class="">.*?<br>(?P<yaer>.*?)&nbsp'
               r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
               r'.*?<span>(?P<person>.*?)人评价</span>',re.S)

result=obj.finditer(content)

f=open("../data.csv",mode="w")

csvwriter=csv.writer(f)

for i in result:

    dic=i.groupdict()

    dic["yaer"]=dic["yaer"].strip()

    csvwriter.writerow(dic.values())

    f.close()
    print("over!!!")
    # print(i.group("name"))
    # print(i.group("rename"))
    # print(i.group("yaer").strip())
    # print(i.group("score"))
    # print(i.group("person"))