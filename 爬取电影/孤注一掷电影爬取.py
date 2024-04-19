import requests
from bs4 import BeautifulSoup
import aiohttp
import aiofiles
import asyncio
from ffmpy import FFmpeg
from Crypto.Cipher import AES
import os
import re


def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    else:
        print("文件夹已创建")


def download_file(url, name):
    resp = requests.get(url)
    with open(name, mode="wb") as f:
        f.write(resp.content)


def get_text(url, name):
    with open(name, mode="r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            secnd_url = str(url) + str(line)
            return secnd_url


async def aio_file_download(file_url):
    tasks = []
    t = 000
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as session:
        async with aiofiles.open("第二层m3u8文件.txt", mode="r", encoding="utf-8") as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                ts_url = str(file_url) + str(line)
                task = asyncio.create_task(download_ts(ts_url, ts_url.split('/')[-1], session))
                t += 1
                tasks.append(task)
            await asyncio.wait(tasks)


async def download_ts(url, ts_name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"ts_viode_01/{ts_name}", mode="wb") as f:
            await f.write(await resp.content.read())
            print(f"{ts_name}----------下载完毕！！")


def get_key(key_url):
    res = requests.get(key_url)
    return res.text


async def aio_des(key):
    tasks = []
    async with aiofiles.open("第二层m3u8文件.txt", mode="r", encoding="utf-8") as f:
        async for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            task = asyncio.create_task(dec_ts(line.split('/')[-1], key))
            tasks.append(task)
        await asyncio.wait(tasks)


async def dec_ts(ts_name, key):  # 密码多长,零有多长
    aes = AES.new(key=key.encode("utf-8"), IV=b'0000000000000000', mode=AES.MODE_CBC)
    async with aiofiles.open(f"ts_viode_01/{ts_name}", mode="rb") as f1, \
            aiofiles.open(f"ts_viode_02/temp_{ts_name}", mode="wb") as f2:  # 解密文件
        bs = await f1.read()  # 从源文件读取内容
        await f2.write(aes.decrypt(bs))  # 把解密好的内容写入文件
        print(f"{ts_name}处理完毕！！！")


def sum():
    with open(f"电影/1.mp4", "wb") as f:
        with open("第二层m3u8文件.txt", "r") as f1:
            for line in f1:
                line = line.strip()
                if line.startswith("#"):
                    continue
                try:
                    with open(f"ts_viode_02/temp_{line}", "rb") as f2:
                        f.write(f2.read())
                except FileNotFoundError:
                    print("文件不存在！")


def mian():
    # link_01 = "https://apitestss.bihee.net/api_v3/vod/detail/" + url.split("=")[1]
    # resp_link = requests.get(link_01).json()
    # # 获取m3u8文件地址
    # file_link = resp_link["data"]["vod_play_urls"][0]["episode"][0]["url"]
    # file_name = resp_link["data"]["vod_name"]
    # # 下载第一层m3u8文件
    # download_file(file_link, "第一层m3u8文件.txt")
    # # 获得第二层m3u8文件的url地址
    # file_links = file_link.split("/20")[0]
    # second_urls = get_text(file_links, "第一层m3u8文件.txt")
    # # 下载第二层m3u8文件
    # second_urls = 'https://newmyg-videomy.004307.com/20210617/EddiLhsL/1500kb/hls/index.m3u8'
    # download_file(second_urls, "第二层m3u8文件.txt")
    # head_second_link = second_urls.split("index.m3u8")[0]
    # # # 下载ts文件
    # asyncio.run(aio_file_download(head_second_link))
    # 获取密码
    # key = get_key(second_urls.split("index.m3u8")[0] + "key.key")
    # 解密
    # asyncio.run(aio_des(key))
    # 合成视频
    sum()


if __name__ == '__main__':
    # url = "https://bihee4.com/play?id=48ce1e903a4a"
    # mkdir("ts_viode_01")
    # mkdir("ts_viode_02")
    # mkdir("电影")
    mian()
