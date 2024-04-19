from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp
import os


def kind_link(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")
    link = soup.find("div", class_="col-sm-6 col-lg-6 item").find_all("a", class_="text-decoration-none text-dark")
    for i in link:
        href = i["href"]
        name = i.text
        newurl = url + href
        list_url.append(newurl)
        list_name.append(f"{link.index(i)}.{name}")


def picture_url(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")
    link = soup.find("div", class_="list-group h6").find_all("a",
                                                             class_="a-list list-group-item list-group-item-action d-flex justify-content-between align-items-center")
    for i in link:
        href = i["href"]
        name = i.text
        names = name.replace("/", "").replace("?", "")
        pic_link = main_url + href
        filename = f"{list_name[num]}/{names}\\"
        if not os.path.exists(filename):
            os.makedirs(filename)
        go_picture(pic_link, filename, name)


def go_picture(url, filename, name):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")
    link = soup.find("div", class_="card-body h4").find_all("img")
    list = []
    for i in link:
        src = i["src"]
        list.append(src)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ex(list, filename, name))


async def aiodownload(url, page, filename, name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as respone:
            with open(filename + str(page) + ".jpg", mode='wb') as f:
                f.write(await respone.content.read())
                print(f"{name}  已完成{page}张！")


async def ex(list, filename, name):
    tasks = []
    page = 0
    for url in list:
        tasks.append(aiodownload(url, page, filename, name))
        page += 1
        if page == len(list):
            break
    await asyncio.wait(tasks)


def main(url):
    global num
    kind_link(url)
    print(list_name)
    num = int(input("请输入你想要看的类型:"))
    urls = list_url[num]
    page = int(input("请输入你想要下载几页？:"))
    for i in range(page, page + 1):
        kink_url = urls + f'/{i}'
        picture_url(kink_url)


if __name__ == '__main__':
    main_url = 'http://puwoktk.org/'
    list_name = []
    list_url = []
    main(main_url)
