# -*-codeing=utf-8-*-
# @Time : 2022/4/25 9:02
# @Author:熊金海
# @File : 电影.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import aiohttp
import aiofiles
import asyncio
# from ffmpy import FFmpeg
from Crypto.Cipher import AES
import os
import re


def get_first_url(url):
    resp = requests.get(url)
    content = resp.text
    soup =  BeautifulSoup(content,"lxml")
    list = soup.find("li",id ="347")
    url = list.a["href"]
    return url


def get_second_url(url):
    resp = requests.get(url)
    content = resp.text
    second_url = re.findall('var now="(.*?)"', content)[0]
    return second_url



def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    else:
        print("文件夹已创建")

def dowmload_m3u8_file(url,name):
    resp =requests.get(url)
    with open(name,mode="wb") as f:
        f.write(resp.content)
async def download_ts(url,name,session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}.ts",mode="wb") as f:
            await f.write(await resp.content.read())
        print(f"{name}下载完毕！！")
async def aio_download():
    tasks=[]
    i=0
    async with aiohttp.ClientSession() as session:#
        async with aiofiles.open("第一集_second.txt",mode="r",encoding="utf-8") as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                i +=1
                task =asyncio.create_task(download_ts(line,i,session))
                tasks.append(task)
            await asyncio.wait(tasks)
def get_key(url):
    resp=requests.get(url)
    return resp.text

# 解码
async def dec_ts(name,key):#密码多长,零有多长
    aes =AES.new(key=key.encode("utf-8"),IV=b'0000000000000000',mode=AES.MODE_CBC)
    async with aiofiles.open(f"video/{name}",mode="rb") as f1,\
        aiofiles.open(f"video1/temp_{name}",mode="wb") as f2:#临时文件
        bs = await f1.read()  #从源文件读取内容
        await f2.write(aes.decrypt(bs))#把解密好的内容写入文件
    print(f"{name}处理完毕！！！")



# 解码
async def aio_dec(key):
    tasks=[]
    async with aiofiles.open("line2.txt",mode="r",encoding="utf-8") as f:
        async for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            line = line.strip()
            #创建异步操作
            task = asyncio.create_task(dec_ts(line,key))
            tasks.append(task)
        await asyncio.wait(tasks)


def mian(url):
    get_first__url = get_first_url(url)
    first_url = url.split("/media")[-2]
    get_first__url_up = first_url+get_first__url #进入视频界面的url
    # print(get_first__url)

    get_second__url=get_second_url(get_first__url_up) #第一层m3u8的url

    head_second_url = get_second__url.split("/20220501")[0]

    dowmload_m3u8_file(get_second__url,"第一集_first.txt")#第一层m3u8文件
    print("第一次下载完毕！！")

    with open("第一集_first.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if line.startswith("#"):
                continue
            first_m3u8_url = head_second_url +line#第二层m3u8d的下载地址

            dowmload_m3u8_file(first_m3u8_url,"第一集_second.txt")#第二层m3u8文件
            print("第二次下载完毕！！")


    # 异步下载文件
    asyncio.run(aio_download())
    # 拿到密钥
    with open("第一集_second.txt",mode="r",encoding="utf-8") as f:
        f = f.read()
        f = str(f)
        url = re.findall('URI="(.*?)"',f)[0]
    #拿到key的地址，并获取 url 为钥匙的网址
    key = get_key(url)
    # print(key)
    # 解密
    asyncio.run(aio_dec(key))
    # 合并
    merge_ts()



if __name__ == '__main__':
    url = 'http://www.youyunliang.com/media/56197.html'
    mkdir("video")
    mian(url)
















