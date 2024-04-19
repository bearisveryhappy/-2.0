# -*-codeing=utf-8-*-
# @Time : 2022/3/27 9:36
# @Author:熊金海
# @File : 百度翻译+post+保存.py
# @Software: PyCharm
import requests
import csv
import re

url='https://fanyi.baidu.com/sug'
head={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047'
}

kw=input("请输入要翻译的单词：")

par={
    "kw": kw
}
f=open("fanyi.json",mode="w")
csvwriter=csv.writer(f)

reps=requests.post(url,data=par,headers=head)
result=[]
content=reps.json()
for i in range(5):
    result0 = content['data'][i]['v']
    result.append(result0)
print(kw+f'翻译的结果为：{result}')
csvwriter.writerow(result)
reps.close()