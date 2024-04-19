# -*-codeing=utf-8-*-
# @Time : 2022/3/25 15:16
# @Author:熊金海
# @File : 百度+写文件.py
# @Software: PyCharm
from urllib.request import urlopen

url="http://www.baidu.com"

reps=urlopen(url)
with open("baidu.html",mode="w") as f :
    f.write(reps.read().decode("utf-8"))
    print("over!!!")
















