# -*-codeing=utf-8-*-
# @Time : 2022/3/31 20:26
# @Author:熊金海
# @File : 5.py
# @Software: PyCharm

import asyncio
import aiohttp
fin1='https://pic.3gbizhi.com/2021/1228/20211228043918694.jpg'
fin2='https://pic.3gbizhi.com/2021/1228/20211228044955257.jpg'
fin3='https://pic.3gbizhi.com/2021/1228/20211228073651948.jpg'
urls = [
    asyncio.create_task(fin1),
    asyncio.create_task(fin2),
    asyncio.create_task(fin3)
]



async def aiodownload(url):
    #发送请求
    #得到图片内容
    #保存到文件
    name = url.rsplit("/",1)[1]#从右边切，切一次，得到[1]位子的内容
    async with aiohttp.ClientSession() as session:#requests
        async with session.get(url) as resp:#resp = requests.get()
            #请求回来写文件
            #可以自己去学一个模块，aiodiles
            with open(name,mode="wb") as f:#创建文件
                f.write(await resp.content.read())#读取内容是异步的，需要await挂起 ， resp.text()


    print(name,"搞定")

async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))


if __name__ == '__main__':
        asyncio.run(main())

















