import requests
from bs4 import BeautifulSoup
import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
def page_request(url):
    reqe=requests.get(url=url,headers=headers,params=params)
    return reqe.text

def page_parse(text,url1):
    soup = BeautifulSoup(text,'html.parser')
    urls = soup.find_all("div",class_="section-box")[1]
    url2 = urls.find_all("a")
    for i in url2:
        name = i.text
        url = i.get("href")
        urls = url.split("/")[-1]
        chapter_names.append(name)
        chapter_urls.append(url1 + urls)


def chapter_page_parse(text):
    soup = BeautifulSoup(text,'html.parser')
    str=''
    chapter_content = soup.find("div",class_="content")
    for i in chapter_content:
        str=str+i.text+"\n"
    return str

def write_file(text, filename):
    with open(filename, "a+",encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == '__main__':
    url = 'http://www.cqwsjds.com/bqg/3808/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
    }
    novel_name = "凡人修仙传"
    chapter_names=[]
    chapter_urls=[]
    params = {}
    text = page_request(url=url)
    page_parse(text,url)
    for chapter_name,chapter_url in zip(chapter_names,chapter_urls):
        chapter_text = page_request(chapter_url)
        time.sleep(3)
        chapter_content = chapter_page_parse(chapter_text)
        write_file(chapter_name+"\n"+chapter_content,novel_name+'.txt')
        print(chapter_name+"已完成")
