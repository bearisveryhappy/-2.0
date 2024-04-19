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
from ffmpy import FFmpeg
from Crypto.Cipher import AES
import os
import re


def get_first_m3u8_url(url):
    resp = requests.get(url)
    content = resp.text
    content = str(content)
    fist_url = re.findall('var now="(.*?)"', content)[0]
    return fist_url


def dowmload_m3u8_file(url, name):
    resp = requests.get(url)
    with open(name, mode="wb") as f:
        f.write(resp.content)


async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}.ts", mode="wb") as f:
            await f.write(await resp.content.read())
        print(f"{name}下载完毕！！")


async def aio_download(up_url):
    tasks = []
    i = 0
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("第一集_second.txt", mode="r", encoding="utf-8") as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                # 拼接.ts真正的路径
                ts_url = str(up_url) + str(line)
                i += 1
                # print(ts_url)
                task = asyncio.create_task(download_ts(ts_url, i, session))
                tasks.append(task)

            await asyncio.wait(tasks)


def get_key(url):
    resp = requests.get(url)
    return resp.text


# 解码
async def dec_ts(name, key):  # 密码多长,零有多长
    aes = AES.new(key=key, iv=b"00000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"video/{name}", mode="rb") as f1, \
            aiofiles.open(f"video/temp_{name}", mode="wb") as f2:
        bs = await f1.read()  # 从源文件读取内容
        await f2.write(aes.decrypt(bs))
    print(f"{name}处理完毕！！！")


# 解码
async def aio_dec(key):
    tasks = []
    async with aiofiles.open("第一集_second.txt", mode="r", encoding="utf-8") as f:
        async for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            line = line.strip()
            # 创建异步操作
            task = asyncio.create_task(download_ts(dec_ts(line, key)))
            tasks.append(task)
        await asyncio.wait(tasks)


def mian(url):
    get_first__url = get_first_m3u8_url(url)  # 第一层m3u8d的下载地址
    ifranme_domain = get_first__url.split("/20210514")[0]

    dowmload_m3u8_file(get_first__url, "第一集_first.txt")  # 第一层m3u8文件
    with open("第一集_first.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            second_m3u8_url = ifranme_domain + line  # 第二层m3u8d的下载地址
            # print(second_m3u8_url)

            dowmload_m3u8_file(second_m3u8_url, "第一集_second.txt")
            print("第二次下载完毕！！")
        #        # print(ifranme_domain)

        second_m3u8_url_up = ifranme_domain
        asyncio.run(aio_download(second_m3u8_url_up))
    # 拿到密钥
    # 拿到key的地址，并获取 url 为钥匙的网址
    key = get_key(url)
    # 解密
    asyncio.run(aio_dec(key))


if __name__ == '__main__':
    url = 'http://www.youyunliang.com/play/1888-0-0.html'
    mian(url)
