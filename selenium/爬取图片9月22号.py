import os
import re

import requests
from bs4 import BeautifulSoup

def page_request(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    req=requests.get(url,headers=headers)
    req.encoding=req.apparent_encoding
    return req

def page_parse_BeautifulSoup(text):
    soup=BeautifulSoup(text,'lxml')
    li_list=soup.find('div',class_='list').find_all('li')
    for li in li_list:
        print(li.a.img['src'])
def write_file(content,filename):
    with open("tupian/"+filename,'wb+') as f:
        f.write(content)
def page_parse_re(text):
    img_lists = re.compile('<img src="(.*?.jpg)" alt=.*?><b>(.*?)</b></a>').findall(text)
    for img,img_name in img_lists:
        img_url=img
        # print(img_url)
        req=page_request(img_url)
        write_file(req.content,img_name+'.jpg')
def mkdir(dirname):
    os.mkdir(dirname)

if __name__ == '__main__':
    url='http://www.netbian.com/fengjing/'
    mkdir('tupian')
    req=page_request(url)
    page_parse_re(req.text)