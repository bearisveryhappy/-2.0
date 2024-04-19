import requests
from bs4 import BeautifulSoup
from Crypto.Cipher import AES
import aiohttp
import aiofiles
import asyncio
import json
import io
import os
import sys
import re

def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    else:
        print("文件夹已创建")
def get_source(url):
    req = requests.get(url)
    return req.text

def download_m3u8_file(url,name):
    resp = requests.get(url)
    with open(f"文件/{name}.txt",mode="wb") as f:
        f.write(resp.content)


async def download_ts(url,number,name,session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"加密/{number}.ts",mode="wb") as f:
            await f.write(await resp.content.read())
        print(f"{number}————————下载完毕！！")

def sum(name):
    with open(f"电影/{name}.mp4", "wb") as f:
        with open(f"文件/{name}002.txt", "r") as f1:
            t = 000
            for line in f1:
                line = line.strip()
                if line.startswith("#"):
                    continue
                with open(f"解密/temp_{t}.ts", "rb") as f2:
                    f.write(f2.read())
                    t += 1
# def sum_02(name):
#     with open(f"电影/{name}.mp4", "wb") as f:
#         with open(f"文件/{name}002.txt", "r") as f1:
#             t = 000
#             for line in f1:
#                 line = line.strip()
#                 if line.startswith("#"):
#                     continue
#                 with open(f"加密/{t}.ts", "rb") as f2:
#                     f.write(f2.read())
#                     t += 1

async def aio_download(up_url,name):
    tasks=[]
    i= 0
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64,ssl=False)) as session:
        async with aiofiles.open(f"文件/{name}002.txt",mode="r",encoding="utf-8") as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                ts_url =str(up_url)+str(line)

                task =asyncio.create_task(download_ts(ts_url,i,name,session))
                i += 1
                tasks.append(task)
            await asyncio.wait(tasks)


async def aio_dec(key,name):
    tasks=[]
    i=0
    async with aiofiles.open(f"文件/{name}002.txt",mode="r",encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            #创建异步操作
            task = asyncio.create_task(dec_ts(i,key))
            i+=1
            tasks.append(task)
        await asyncio.wait(tasks)

def get_key(url):
    req = requests.get(url)
    return req.text

async def dec_ts(i,key):#密码多长,零有多长
    aes =AES.new(key=key,IV=b"0000000000000000",mode=AES.MODE_CBC)
    async with aiofiles.open(f"加密/{i}.ts",mode="rb") as f1,\
        aiofiles.open(f"解密/temp_{i}.ts",mode="wb") as f2:
        content = await f1.read()  #从源文件读取内容
        bs = aes.decrypt(content)
        await f2.write(bs)
    print(f"{i}————————解密完毕！！！")
def second(url):
    resp = requests.get(url).json()
    image = resp["data"]
    name= image["vod_name"]
    art_content = image["vod_play_urls"][0]["episode"][0]["url"]
    download_m3u8_file(art_content,name+'001')
    print("第一次下载完毕！！")
    with open(f"文件/{name}001.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            second_m3u8_url = art_content.split("/20")[0] + line  # 第二层m3u8d的下载地址
            download_m3u8_file(second_m3u8_url,name+"002")
            print("第二次下载完毕！！")

    second_m3u8_url_up = second_m3u8_url.split("/20")[0]
    asyncio.run(aio_download(second_m3u8_url_up,name))

    key = second_m3u8_url.split("index.m3u8")[0] + "key.key"
    key = get_key(key)
    asyncio.run(aio_dec(key.encode('utf-8'),name))
    sum(name)

def main(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,"html.parser")
    link = soup.find("div",class_="c-caUZiY").find_all('a',class_="c-bfGGms")
    for i in link:
        href = i["href"]
        digital = href.split("id=")[1]
        head_url = 'https://api2.bebox.live/api_v3/vod/detail/'
        all_url = head_url+digital
        second(all_url)


if __name__ == '__main__':
    words = input("请输入你想过要的页数：")
    url = f'https://www.bihe8.me/list/all/{words}'
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    mkdir("加密")
    mkdir("解密")
    mkdir("文件")
    mkdir("电影")
    main(url)








