# -*-codeing=utf-8-*-
# @Time : 2022/4/25 19:28
# @Author:熊金海
# @File : 爬取电影.py
# @Software: PyCharm
import requests
import aiohttp
import aiofiles
import asyncio
# from ffmpy import FFmpeg
import os
import re


def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    else:
        print("文件夹已创建")


def first_url(url):
    # resp = requests.get(url)
    # content = resp.text
    # content = str(content)
    # first_url = re.findall('var src = "(.*?)"',content)[0]
    first_url_up = 'https://cp.pavidcdn.com/stream/full/asia/700/91CM-223.m3u8'
    return first_url_up


def download_m3u8_file(url, name):
    resp = requests.get(url)
    with open(name, mode="wb") as f:
        f.write(resp.content)
        print("下载完毕！！")


async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}.ts", mode="wb") as f:
            await f.write(await resp.content.read())
        print(f"{name}下载完毕！！")


def sum():
    with open("01.mp4", "wb") as f:
        with open("end.txt", "r") as f1:
            t = 000
            for line in f1:
                line = line.strip()
                if line.startswith("#"):
                    continue
                with open("video/{}.ts".format(t), "rb") as f2:
                    f.write(f2.read())
                    t += 1


async def aio_download(up_url):
    tasks = []
    i = 000
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("end.txt", mode="r", encoding="utf-8") as f:
            async for line in f:
                line = line.strip('')
                if line.startswith("#"):
                    continue
                # 拼接.ts真正的路径
                ts_url = str(up_url) + str(line)
                # i = line.split("/")[-1]
                task = asyncio.create_task(download_ts(ts_url, i, session))
                i += 1
                tasks.append(task)
            await asyncio.wait(tasks)


def main(url):
    get_first_url = first_url(url)
    download_m3u8_file(get_first_url, "end.txt")
    second_m3u8_url = get_first_url.split("91CM-223.m3u8")[0]
    asyncio.run(aio_download(second_m3u8_url))
    sum()


if __name__ == '__main__':
    url = 'http://bbee00.xyz/dp/show/nm1r2s'
    main(url)
