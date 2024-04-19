# -*-codeing=utf-8-*-
# @Time : 2022/3/30 19:31
# @Author:熊金海
# @File : 4.py
# @Software: PyCharm
import requests
from lxml import etree
import sys
import io
import csv

def mian(url):
    resp=requests.get(url)
    resp.encoding="utf-8"
    f=open("../猪八戒求职信息.txt", mode="w")
    csvwriter=csv.writer(f)
    html = etree.HTML(resp.text)
    divs=html.xpath('/html/body/div[1]/div/div/div[5]/div/div[2]/section[1]/ul/li')

    for div in divs:
        title=div.xpath('./div/div[1]/div[1]/div[1]/div[1]/text()')[0]
        location=div.xpath('./div/div[1]/div[1]/div[1]/div[2]/text()')[0]
        xueli=div.xpath('./div/div[1]/div[1]/div[2]/div[4]/text()')[0]
        salary=div.xpath('./div/div[1]/div[1]/div[2]/div[1]/text()')[0]
        yaer=div.xpath('./div/div[1]/div[1]/div[2]/div[2]/text()')[0]
        conpany=div.xpath('./div/div[1]/div[2]/div[2]/div[1]/text()')[0]
        csvwriter.writerow([title,location,xueli,conpany,salary,yaer])



if __name__ == '__main__':
    i=input("请输入一个职业：")
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    mian(url=f'https://zp.zbj.com/search/all?kw={i}')
