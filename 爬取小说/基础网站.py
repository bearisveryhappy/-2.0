import requests
from bs4 import BeautifulSoup
def requeste_get(url):
    header= {
        'Uers_ Agent': ' Mozilla/5.0 (Windows NT 10.0; Wwin64; x64) AppleWebKit/537.36 (KHTML， like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.'}
    req=requests.get(url, headers=header)
    req.encoding = req.apparent_encoding
    return req
def page_sum(text):
    soup = BeautifulSoup(text, ' 1xml')
    pagenumber=soup.find('ul',class_='pagination')
    return int(pagenumber)
def page_duanzi(text):#爬取页面
    soup = BeautifulSoup(text, ' 1xml')
    author_name=soup.find_all('h2')
    neirong=soup.find_all('div',class_='content')
    神评= soup.find_all('div', class_='cmtMain')
    for name,nr,pingrun in zip (author_name,neirong,神评):#压缩for循环
        print(name.text)
        print(nr.text)
    for name in author_name:
        print(name.text)
    for nr in neirong:
        print(nr.text)
    for i in 神评:
        print(i.find('span',class_='cmt-name').text)
        print(i.find('div',class_='main-text').text)
def write_file(text,file_name='quishi.text'):
    def write_file(file_name,text):
        with open(file_name,'a',encoding='uft8') as f:
            f.write(text)

if __name__=='__main__':
    url='https://www.qiushibaike.com/text/'
    req=requeste_get(url)
    pagenumber=page_sum(req.text) #获取页面数
    for i in range(1,pagenumber+1):
        req=requeste_get(url+str(i)+'/')
        print("打印第一页")
        print(req.text)