import requests
from bs4 import BeautifulSoup
import os
import asyncio
import aiohttp

async def page(url, name):
    each_album_all = requests.get(url).json()
    for i in each_album_all['data']['list']:
        id = i['art_id']
        url = f'https://apitestss.bihee.net/api_v3/image/detail/{id}'
        req = requests.get(url).json()
        content = req['data']['art_content']
        name_page = req['data']['art_name']
        filename = f"{name}/{name_page}\\"
        if not os.path.exists(filename):
            os.makedirs(filename)
        tasks = []
        page = 0
        for i in content:
            tasks.append(aiodownload(i, filename, page))
            page += 1
        await asyncio.wait(tasks)


async def aiodownload(picture_url, filename, page):
    async with aiohttp.ClientSession() as session:
        async with session.get(picture_url) as respone:
            with open(filename + str(page) + ".jpg", mode='wb') as f:
                f.write(await respone.content.read())
                print(f"{name_page}----------已完成{page}张！")


def main(url):
    req = requests.get(url).json()
    print(req['data']['main'][1]['class']['list'])
    choose = int(input("请输入你想要的序号："))
    main_content = req['data']['main'][1]['class']['list'][choose]
    id = main_content["type_id"]
    name = main_content["type_name"]  # 漫画
    page_1 = input("请输入你想要的页数：")
    manhua_url = f'https://apitestss.bihee.net/api_v3/image/list?type_id={id}&pageSize=24&page={page_1}'
    asyncio.run(page(manhua_url, name))
if __name__ == '__main__':
    url = 'https://apitestss.bihee.net/api_v3/create/index/beabox2023'
    main(url)
