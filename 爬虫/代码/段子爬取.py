import requests
from bs4 import BeautifulSoup

def request_get(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    req=requests.get(url,headers=header)
    req.encoding=req.apparent_encoding
    return req
def page_sum(text):
    soup=BeautifulSoup(text,'lxml')
    pagenumber=soup.find('ul',class_='pagination').find_all('li')[-2].a.span.text
    return int(pagenumber)
def page_duanzi(text):#爬取页面的段子
    soup=BeautifulSoup(text,'lxml')
    author_name=soup.find_all('h2')
    内容=soup.find_all('div',class_='content')
    神评=soup.find_all('div',class_='cmtMain')
    for name,neirong,pinglun in zip(author_name,内容,神评):
        write_file(name.text.strip(),'qiushi1.txt')
        write_file(neirong.text.strip())
        write_file(pinglun.find('span', class_='cmt-name').text.strip())
        write_file("".join(pinglun.find('div', class_="main-text").text.split()))
def write_file(text,file_name='qiushi.txt'):
    with open(file_name,'a+',encoding='utf-8') as f:
        f.write(text+'\n')
if __name__ == '__main__':
    url_base='https://www.qiushibaike.com/text/page/'
    req=request_get(url_base)
    pagenumber=page_sum(req.text)#获取页面数
    for i in range(1,pagenumber+1):
        req=request_get(url_base+str(i)+'/')
        page_duanzi(req.text)