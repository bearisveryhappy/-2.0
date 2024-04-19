# -*-codeing=utf-8-*-
# @Time : 2022/3/30 18:35
# @Author:熊金海
# @File : 3.py
# @Software: PyCharm
import io
import sys
import requests
from bs4 import BeautifulSoup
from lxml import etree

def mian(url,par):
    resp = requests.post(url,data=par)
    resp.encoding="utf-8"

    dic=resp.json()
    for  list in dic['list']:
        name=list['prodName']
        print(name)






if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    par = {
        'limit': 20,
        'current': 1,
        'pubDateStartTime': '',
        'pubDateEndTime': '',
        'prodPcatid': '',
        'prodCatid': '',
        'prodName': '',
    }
    mian(url, par)

























































