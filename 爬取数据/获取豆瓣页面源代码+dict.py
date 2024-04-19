# -*-codeing=utf-8-*-
# @Time : 2022/3/25 17:29
# @Author:熊金海
# @File : 获取豆瓣页面源代码+dict.py
# @Software: PyCharm
import requests

url="https://movie.douban.com/typerank"
i=input("输入电影类型(例如：喜剧)：")
dic={
    'type_name': i,
    'type': '24',
    'interval_id': '100:90',
    'action': ''
}

head={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
}

resp=requests.get(url=url,headers=head,params=dic)
print(resp.text)
resp.close()