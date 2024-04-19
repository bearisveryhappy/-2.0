# -*-codeing=utf-8-*-
# @Time : 2022/4/23 18:16
# @Author:熊金海
# @File : 爬取网易云.py
# @Software: PyCharm

import requests
import re
import os
import json

filename = '热歌榜\\'

if not os.path.exists(filename):
    os.mkdir(filename)


header ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
    }
url = 'https://music.163.com/dis cover/toplist?id=3778678'
resp = requests.get(url,headers=header)

info_list =re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>',resp.text)
# print(resp.text)
for music_id,name in info_list:

    music_url=f"http://music.163.com/song/media/outer/url?id={music_id}.mp3"
    # print(music_url)
    music_resp = requests.get(url=music_url,headers=header).content

    with open(filename + name + '.mp3', mode='wb+') as f :
        f.write(music_resp)
    print(music_id,name)