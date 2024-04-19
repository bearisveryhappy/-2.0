# -*-codeing=utf-8-*-
# @Time : 2022/3/27 12:02
# @Author:�ܽ�
# @File : 爬取电影天堂+re.py
# @Software: PyCharm
import requests
import re

url = 'https://www.dydytt.net/index2.htm'
resp=requests.get(url,verify=False)
resp.encoding="gbk"
# print(resp.text)

obj1=re.compile(r"游戏资源下载.*?<ul>(?P<ul>.*?)<ul>",re.S)

obj2=re.compile(r"<a href='(?P<href>.*?)'",re.S)

obj3=re.compile(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">.*?'
                r'<a href="#" target="_self" thunderpid="" thundertype="" thunderrestitle="(?P<download>.*?)">',re.S)

result1=obj1.finditer(resp.text)
href_list=[]
for it in result1:
     ul=it.group("ul")

     result2=obj2.finditer(ul)
     for itt in result2:
         print(itt.group("href"))
         child_href=url +itt.group("herf")
         href_list.append(child_href)

for href in href_list:
    child_resp=requests.get(href,verify=False)
    child_resp.encoding="gbk"
    result3=obj3.search(child_resp.text)
    print(result3.group("download"))



