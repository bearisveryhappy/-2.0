# -*-codeing=utf-8-*-
# @Time : 2022/4/22 19:56
# @Author:熊金海
# @File : 爬取酷我音乐.py
# @Software: PyCharm
import requests
import os
import json

headers ={
    'ser-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31',
    'Referer':'https://kuwo.cn/rankList',
    'csrf': 'HC5O18GGZ2W',
    'Cookie':'Hm_Iuvt_cdb524f42f0cer9b268e4v7y734w5esq24 = 8N2YjR3BHGMQad5znrhiAAF5E2bKT77Z'
}

# singer = input("请输入歌手名：")
# url= f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={singer}'
urls  ="https://kuwo.cn/api/www/bang/bang/musicList?bangId=16&pn=1&rn=20&httpsStatus=1&reqId=3c3a5610-5853-11ee-b33b-955fc071dc6c&plat=web_www&from="
result =requests.get(urls,headers=headers).json()

filename = '好听\\'

if not os.path.exists(filename):
    os.mkdir(filename)

data = result['data']['musicList']

for i in data:
    name =i['name']
    rid = i['rid']
    url2 = f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={rid}&type=music&httpsStatus=1&reqId=c93411c1-c239-11ec-bfe4-bbe6535ee566'
    result2 =requests.get(url2,headers=headers).json()
    if result2['success']== False:
        continue
    else:
        url = result2['data']['url']
        with open(f"{filename}/{name}.mp3","wb") as f :
            print(f"正在下载{name}",end='')
            music = requests.get(url)
            f.write(music.content)
            f.close()
            print("\t下载完成！！")
