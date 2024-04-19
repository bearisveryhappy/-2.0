import requests
from bs4 import BeautifulSoup
import aiohttp
import aiofiles
import asyncio
import os
import re
def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    else:
        print("文件夹已创建")
def page(url):
    req = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(req.text,"html.parser")
    link = soup.find('ul',class_="videoContent").find_all('li')
    list = []
    for i in link:
        href = i.a['href']
        title = i.a.text
        list.append(href)
        list.append(title)
    return list

def first_m3u8(url):
    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text,"html.parser")
    link = soup.find('div',class_="playlist wbox ffm3u8").find_all('li')
    list = []
    for i in link[:-1]:
        href = i.a['href']
        chapter = i.a['title']
        list.append(href)
        list.append(chapter)
    return list
def download_m3u8_file(url,name):
    resp = requests.get(url)
    with open(name,mode="wb") as f:
        f.write(resp.content)
        print("下载完毕！！")
async def aio_download(up_url):
    tasks=[]
    i=0
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64,ssl=False)) as session:
        async with aiofiles.open("second.txt",mode="r",encoding="utf-8") as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                #拼接.ts真正的路径
                ts_url =str(up_url)+str(line)
                task =asyncio.create_task(download_ts(ts_url,i,session))
                i +=1
                tasks.append(task)
            await asyncio.wait(tasks)
async def download_ts(url,name,session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}.ts",mode="wb") as f:
            await f.write(await resp.content.read())
        print(f"{name}--------下载完毕！！")
def sum(i,header_name):
    with open(f"{header_name}/{i}.mp4", "wb") as f:
        with open("second.txt", "r") as f1:
            t = 000
            for line in f1:
                line = line.strip()
                if line.startswith("#"):
                    continue
                with open(f"video/{t}.ts", "rb") as f2:
                    f.write(f2.read())
                    t += 1
def video_download(m3u8_list,header_name):
    num =1
    for i in m3u8_list[0::2]:
        download_m3u8_file(i,"first.txt")
        with open("first.txt", mode="r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                second_m3u8_url = i.split('index.m3u8')[0] + line  # 第二层m3u8d的下载地址
                download_m3u8_file(second_m3u8_url,"second.txt")
            second_m3u8_url_up = second_m3u8_url.split("index.m3u8")[0]
            asyncio.run(aio_download(second_m3u8_url_up))
            sum(num,header_name)
            num += 1
def main(url):
    list = page(url)
    print(list[1::2])
    word =int(input("请输入序号："))
    header_url = url.split("/index")[0] + list[::2][word]
    header_name = list[1::2][word].replace("|","")
    mkdir(header_name)
    m3u8_list = first_m3u8(header_url)
    video_download(m3u8_list,header_name)


if __name__ == '__main__':
    words = input("请输入你想要的电影：")
    url = f'http://ffzy4.tv/index.php/vod/search.html?wd={words}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }
    mkdir("video")
    main(url)
