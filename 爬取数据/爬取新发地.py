# -*-codeing=utf-8-*-
# @Time : 2022/4/24 20:26
# @Author:熊金海
# @File : 爬取新发地.py
# @Software: PyCharm
import requests
import json
import csv

url ='http://www.xinfadi.com.cn/getCat.html'
data ={
    'prodCatid': 1186
}
resp =requests.post(url,data=data).json()

f=open("菜价.csv", mode="w")
csvwriter=csv.writer(f)

for i in range(0,39):
    kind = resp["list"][i]["prodCat"]
    name = resp["list"][i]["prodName"]
    date = resp["list"][i]["pubDate"]
    info = resp["list"][i]["unitInfo"]
    high = resp["list"][i]["highPrice"]
    low = resp["list"][i]["lowPrice"]
    aver = resp["list"][i]["avgPrice"]
    csvwriter.writerow([name,low,aver,high,info,kind,date])

f.close()
print("over~!!")
