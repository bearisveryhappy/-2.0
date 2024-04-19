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
def url_page(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    page = soup.find("ul", class_="videoContent").find_all("a")
    content = str(page)
    first_url = re.findall('<a class="videoName" href="(.*?)" style="width:370px;" target="_blank">', content)
    movie_name = re.findall('target="_blank">(.*?)</i>', content)
    dig = 0
    list = []
    for i in range(0,len(first_url)):
        box = url.split("/index.php")[0] + first_url[dig] + "+" + movie_name[dig]
        list.append(box)
        dig+=1
    return list
def ac_m3u8(url):
    choose = int(input("请输入你想要的电影位数:"))
    content = url[choose]
    contents =str(content)
    name = contents.split("+")[1]
    req = requests.get(contents.split("+")[0])
    soup = BeautifulSoup(req.text, "html.parser")
    page = soup.find("div", class_="playlist wbox ffm3u8").find_all("li")
    content = str(page)
    second_name = re.findall('<a href="(.*?)" target="_blank" title="第.*?集"><font color="red">',content)
    second_name.append(name)
    if len(second_name) == 0:
        pass
    else:
        return second_name
def download_m3u8_file(url, file_name):
    resp = requests.get(url)
    with open(file_name, mode="wb") as f:
        f.write(resp.content)
async def aio_download(second_m3u8_url):
    tasks = []
    i = 0
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("second.txt", mode="r", encoding="utf-8") as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                lines = second_m3u8_url.split("mixed.m3u8")[0] + str(line)
                task = asyncio.create_task(download_ts(lines, i, session))
                i += 1
                tasks.append(task)
            await asyncio.wait(tasks)


async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}.ts", mode="wb") as f:
            await f.write(await resp.content.read())
        print(f"{name}下载完毕！！")


def sum(name):
    with open(f"{name}.mp4", "wb") as f:
        with open("second.txt", "r") as f1:
            t = 000
            for line in f1:
                line = line.strip()
                if line.startswith("#"):
                    continue
                with open("video/{}.ts".format(t), "rb") as f2:
                    f.write(f2.read())
                    t += 1
def main(url):
    box = url_page(url)
    print(box)
    m3u8_url = ac_m3u8(box)
    download_m3u8_file(m3u8_url[0],"first.txt")
    print("第一次下载完毕！！")
    with open("first.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            second_m3u8_url = str(m3u8_url[0]).split("index.m3u8")[0] + str(line)
            download_m3u8_file(second_m3u8_url,"second.txt")
            print("第二次下载完毕！！")
        asyncio.run(aio_download(second_m3u8_url))
        movie_name = m3u8_url[1]
        mkdir(movie_name)
        sum(movie_name)
if __name__ == '__main__':
    name = input("你想要的电影或者演员名：")
    page = int(input("请输入你想要的页数："))
    url = f'http://ffzy5.tv/index.php/vod/search/page/{page}/wd/{name}.html'
    main(url)