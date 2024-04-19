import requests
from bs4 import BeautifulSoup
import aiohttp
import aiofiles
import asyncio
# from ffmpy import FFmpeg
from Crypto.Cipher import AES
import os
import re


def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    else:
        print("文件夹已创建")


def tail_link(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    link = soup.find('div', class_="module-items module-card-items").find_all("div", class_="module-card-item-title")
    list = []
    for i in link:
        href_url = i.a['href']
        name = i.text
        list.append(href_url)
        list.append(name)
    return list


def get_link(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    link = soup.find('div', class_="module-play-list").find_all('a')
    list = []
    for i in link:
        href_url = i["href"]
        name = i.text
        list.append(href_url)
        list.append(name)
    return list


# 第一层链接
def get_first_url(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    page = soup.find("div", class_="player-box-main").find_all("script")
    content = str(page)
    first_url = re.findall('.*?"url":"(.*?)".*?', content)
    first_url = first_url[0].replace("\\", "")
    get_second_url(first_url)


def get_second_url(url):
    download_file(url, "first.txt")
    print("第一次下载完毕！！")
    with open("first.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            second_m3u8_url = str(url.split("index.m3u8")[0]) + str(line)
            download_file(second_m3u8_url, "second.txt")
            print("第二次下载完毕！！")
        asyncio.run(aio_download(second_m3u8_url))


async def aio_download(second_m3u8_url):
    tasks = []
    i = 0
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as session:
        async with aiofiles.open("second.txt", mode="r", encoding="utf-8") as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                lines = str(second_m3u8_url.split("mixed.m3u8")[0]) + str(line)
                task = asyncio.create_task(download_ts(lines, i, session))
                i += 1
                tasks.append(task)
            await asyncio.wait(tasks)


async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}.ts", mode="wb") as f:
            await f.write(await resp.content.read())
        print(f"第{name}段————————————下载完毕！！")


def download_file(url, name):
    resp = requests.get(url)
    with open(name, mode="wb") as f:
        f.write(resp.content)


def sum_movie(main_name, name):
    with open(f"{main_name}/第{name}集.mp4", "wb") as f:
        with open("second.txt", "r") as f1:
            t = 000
            for line in f1:
                line = line.strip()
                if line.startswith("#"):
                    continue
                with open(f"video/{t}.ts", "rb") as f2:
                    f.write(f2.read())
                    t += 1


def main(url):
    list = tail_link(url)
    print(list[1::2])
    num = int(input("请输入想看电影的序号："))
    page_url = url.split("/s/")[0] + list[::2][num]  # 页面的链接
    mkdir(list[1::2][num])

    # 获取每一集的链接
    list_link = get_link(page_url)
    t = 1
    for i in list_link[::2]:
        ever_chapter = url.split("/s/")[0] + i
        get_first_url(ever_chapter)
        sum_movie(list[1::2][num], t)
        t += 1


if __name__ == '__main__':
    movie_name = input("请输入想要看的电影名字：")
    url = f'https://www.ppys66.com/s/{movie_name}-------------.html'
    mkdir("video")
    main(url)
