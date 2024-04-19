import asyncio
import aiohttp

urls = [
    'https://scpic3.chinaz.net/Files/pic/pic9/202108/apic34826_s.jpg',
    'https://scpic3.chinaz.net/Files/pic/pic9/202108/apic34828_s.jpg',
    'https://scpic3.chinaz.net/Files/pic/pic9/202108/apic34825_s.jpg'
]

async def aiodownload(url):
    name = url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as respone:
             with open(name,mode='wb') as f:
                f.write(await respone.content.read())

async def ex():
    for url in urls:
        await asyncio.create_task(aiodownload(url))

if __name__ == "__main__":
    asyncio.run(ex())