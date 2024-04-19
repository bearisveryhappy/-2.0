#爬取起点小说
import requests
from bs4 import BeautifulSoup


def page_request(url):
    req=requests.get(url=url,headers=headers,params=params)
    req.encoding=req.apparent_encoding
    return req.text

#解析网页结构,BeautifulSoup方式 获取各个章节名称和url放入列表中
def page_parse(text):
    soup=BeautifulSoup(text,'lxml')
    uls=soup.find('div',class_="volume-wrap").findChildren("ul",class_="cf")
    for ul in uls:
        lis=ul.findAll("li")
        for li in lis:
            chapter_names.append(li.a.text)
            chapter_urls.append("http:"+li.a["href"])

#解析章节页面结构，提取章节内容
def chapter_page_parse(text):
    soup = BeautifulSoup(text, 'lxml')
    str=''
    chapter_content = soup.find("div", class_="read-content j_readContent").findChildren("p")
    for i in chapter_content:
        str=str+i.text+"\n"
    return str
# 写入文件
def write_file(text, filename):
    with open(filename, "a+",encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == '__main__':
    url="https://book.qidian.com/info/3267635/#Catalog"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    novel_name = "混沌记"
    chapter_names=[]
    chapter_urls=[]
    params = {}
    text = page_request(url=url)
    page_parse(text)
    for chapter_name,chapter_url in zip(chapter_names,chapter_urls):
        chapter_text=page_request(chapter_url)
        chapter_content=chapter_page_parse(chapter_text)
        write_file(chapter_name+"\n"+chapter_content,novel_name+'.txt')
        print(chapter_name+"已完成")
