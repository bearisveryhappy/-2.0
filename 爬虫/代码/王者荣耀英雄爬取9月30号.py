import json
import os
import re
from bs4 import BeautifulSoup
import requests


def page_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'
    }
    params={
    }
    req=requests.get(url,headers=headers,params=params)
    req.encoding=req.apparent_encoding
    return req
def page_herolist(text):

    soup=BeautifulSoup(text,'lxml')
    herolist_div=soup.find("div",class_="herolist-content").findAll('li')
    for hero in herolist_div:
        hero_name.append(hero.a.text)
        hero_pic.append('http:'+hero.a.img['src'])
        hero_url.append(hero.a['href'])
def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
def removefile(filename):
    if os.path.exists(filename):
        os.remove(filename)
def write_file(content,filename,file_dirname):
    with open(file_dirname+filename,'wb+') as f:
        f.write(content)
def write_file_txt(text):
    with open('../英雄技能描述.txt', 'a+') as f:
        f.writelines(text+"\n")
def hero_jineng(hero_name,hero_pic,hero_url,hero_type):
    pic = page_request(hero_pic).content
    write_file(pic, hero_name + '.jpg', hero_type+'/')
    req = page_request("https://pvp.qq.com/web201605/" + hero_url)
    div_list = BeautifulSoup(req.text, 'lxml').findAll('div', class_="show-list")
    write_file_txt("英雄：" + i)
    jineng_num = 1
    for div in div_list:
        if div.p.b.text != '':
            print(div.p.text)
            print(div.find("p", class_='skill-desc').text)
            write_file_txt("第" + str(jineng_num) + "技能：" + div.p.text)
            write_file_txt("技能描述：" + div.find("p", class_='skill-desc').text)
            jineng_num = jineng_num + 1
if __name__ == '__main__':
    url_herolist="https://pvp.qq.com/web201605/herolist.shtml"
    url_herojson="https://pvp.qq.com/web201605/js/herolist.json"
    hero_name=[]
    hero_pic=[]
    hero_url=[]
    hero_type=[]
    req=page_request(url_herolist)
    page_herolist(req.text)
    req_json=page_request(url_herojson)
    hero_json=json.loads(req_json.text)
    for hero in hero_name:
        for i in hero_json:
            if hero==i['cname']:
                hero_type.append(i['hero_type'])
    herohype_list=["战士",'法师','坦克','刺客',"射手",'辅助']
    for herohype in herohype_list:
        mkdir(herohype)
    removefile("../英雄技能描述.txt")
    for i,j,k,m in zip(hero_name,hero_pic,hero_url,hero_type):
        hero_jineng(i,j,k,herohype_list[m-1])
