# -*-codeing=utf-8-*-
# @Time : 2022/3/27 9:58
# @Author:熊金海
# @File : 保存百度网页.py
# @Software: PyCharm
from  urllib.request import urlopen
import requests
import urllib.request,urllib.error

url='http://www.baidu.com'
response=urlopen(url)

with open("../baidu1.html", mode="w") as f:
    f.write(response.read().decode("utf-8"))

    response.close

