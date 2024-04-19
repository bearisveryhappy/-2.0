# -*-codeing=utf-8-*-
# @Time : 2022/3/6 10:00
# @Author:熊金海
# @File : 猎聘爬取.py
# @Software: PyCharm
import csv
import io
import re
import sys

import requests
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
x = str((input("请输入你要查询的职位：")))
y = int(input("请输入你要查询的页数："))

url = 'https://www.liepin.com/zhaopin/'
head={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
}
dic={
    'headId': '9e19eb69b66686a1fc0b45ab17baafdf',
    'ckId': 'mr2npaecnjxe9zpfpt31d2zwn8x5m3ga',
    'oldCkId':'9e19eb69b66686a1fc0b45ab17baafdf',
    'fkId': 'bsxqj7mociqr5zv0t3etc229mgr2wn08',
    'skId': 'bsxqj7mociqr5zv0t3etc229mgr2wn08',
    'sfrom': 'search_job_pc',
    'key':'x',
    'currentPage':y ,
    'scene': 'page'
}
resp = requests.get(url,headers=head,params=dic)
resp.encoding="utf-8"

f= open("../猎聘爬取.json", mode='w')
csvwriter=csv.writer(f)
content=resp.text


findR=re.compile(r'<span class="ellipsis-1">(.*?)</span>',re.S)
findS=re.compile(r'<span class="job-salary">(.*?)</span>',re.S)
findT=re.compile(r'<div title="(.*?)"',re.S)
findF=re.compile(r'<span class="labels-tag">(.*?)</span>',re.S)
findC=re.compile(r'<div class="company-tags-box ellipsis-1">.*?<span>(.*?)</span>.*?</div>',re.S)
findN=re.compile(r'<span class="company-name ellipsis-1">(.*?)</span>',re.S)

soup = BeautifulSoup(content,"html.parser")
for item in soup.find_all("div",class_="job-list-item"):
    item=str(item)

    replace=re.findall(findR,item)[0]   #工作城市
    salary=re.findall(findS,item)[0]    #工作薪资
    company=re.findall(findT,item)       #工作名称
    fuli = re.findall(findF,item)       #工作福利
    kind=re.findall(findC,item)   #工作类型
    name=re.findall(findN,item)[0]      #工作公司
    dict=(replace,salary,fuli,name,kind)

    csvwriter.writerow(dict)
    print("爬取完毕！！！")


