import requests
from bs4 import BeautifulSoup
import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def page_request(url):
    reqe=requests.get(url=url,headers=headers)
    return reqe.text

def page_parse(text,url1):
    soup = BeautifulSoup(text,'html.parser')
    urls = soup.find_all("div",class_="list")[0]
    url2 = urls.find_all("a")
    for i in url2:
        name = i.text
        url = i.get("href")
        url3 = url.split(url1.split("/")[-1])[-1]
        chapter_names.append(name)
        chapter_urls.append(url1 + url3)

def chapter_page_parse(text):
    soup = BeautifulSoup(text,'html.parser')
    str=''
    chapter_content = soup.find("div",class_="text")
    for i in chapter_content:
        str=str+i.text+"\n"
    return str.strip()

def write_file(text, filename):
    with open(filename, "a+",encoding="utf-8") as f:
        f.write(text)

if __name__ == '__main__':
    url = 'https://www.biquge7.xyz/34819'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
    }
    novel_name = "斗破苍穹"
    chapter_names=[]
    chapter_urls=[]
    text = page_request(url=url)
    page_parse(text,url)
    for chapter_name,chapter_url in zip(chapter_names,chapter_urls):
        chapter_text = page_request(chapter_url)
        time.sleep(3)
        chapter_content = chapter_page_parse(chapter_text).strip("\n")
        write_file("\n"+chapter_name+"\n"+chapter_content,novel_name+'.txt')
        print(chapter_name+"已完成")
