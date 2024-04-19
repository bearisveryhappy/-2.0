import asyncio
import os
import re
from time import sleep

import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup


def get_text(url):
    r = requests.get(url)
    return r.text


def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    else:
        print(f"{dirname}文件夹已创建")


def area(url):
    soup = BeautifulSoup(get_text(url), 'html.parser')
    later_link = soup.find('div', class_='row features').find_all('p', class_='description')[1].find_all('a')
    for i in later_link:
        area_href = url + i['href']
        area_text = i.text
        area_names.append(area_text)
        area_links.append(area_href)


def get_link(kind,type_video):
    soup = BeautifulSoup(get_text(f"{area_links[kind]}/{type_video}"), 'html.parser')
    link = soup.find('div', class_='row').find_all('a', class_='card-link')
    for k in link:
        later_link = url + k['href']
        name = k.text.strip()
        video_link.append(later_link)
        video_name.append(name)


def get_video_m3u8(url):
    content = get_text(url)
    first_url = re.findall('var src = "(.*?)"', str(content))[0].replace('\/', '/')
    return first_url


def download_m3u8_file(url, name):
    resp = requests.get(url)
    with open(f"files/{name}", mode="wb") as f:
        f.write(resp.content)
        print(f"{name},下载完毕！！")


async def download_ts(url, ts_name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{ts_name}.ts", mode="wb") as f:
            await f.write(await resp.content.read())
        print(f"{ts_name}下载完毕！！")


async def aio_download(up_url, name):
    tasks = []
    t = 000
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(f"files/{name}", mode="r", encoding="utf-8") as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                # 拼接.ts真正的路径
                ts_url = str(up_url.split(line.split('/')[0])[0]) + str(line)
                task = asyncio.create_task(download_ts(ts_url, t, session))
                t += 1
                tasks.append(task)
            await asyncio.wait(tasks)


def video_sum(files_name):
    with open(f"m3u8s/{files_name}.mp4", "wb") as f:
        with open(f"files/{files_name}.txt", "r") as f1:
            t = 7
            for line in f1:
                line = line.strip()
                if line.startswith("#"):
                    continue
                try:
                    with open(f"video/{t}.ts", "rb") as f2:
                        f.write(f2.read())
                        t += 1
                except FileNotFoundError:
                    print("文件不存在！")


if __name__ == '__main__':
    area_names = []
    area_links = []
    video_link = []
    video_name = []
    url = 'http://puwoktk.org'
    area(url)
    print('[', end='')
    for i in area_names:
        if i == area_names[-1]:
            print(str(area_names.index(i) + 1) + '.' + i, end='')
        else:
            print(str(area_names.index(i) + 1) + '.' + i + ',', end='')
    print(']')
    kind = int(input("请输入你想要看的类型：")) - 1
    type_video = int(input("请输入你要下载第几页？："))
    mkdir('video')
    mkdir('m3u8s')
    mkdir('files')
    get_link(kind,type_video)
    print(video_name)
    for v_url, v_name in zip(video_link, video_name):
        m3u8_file = get_video_m3u8(v_url)
        download_m3u8_file(m3u8_file, v_name + '.txt')
        asyncio.run(aio_download(m3u8_file, v_name + '.txt'))
        video_sum(v_name)
        print(f"{v_name},已经下载完成！！！")
        sleep(5)
    print("恭喜你，视频全都下载完成！！！")
