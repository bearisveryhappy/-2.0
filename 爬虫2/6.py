# -*-codeing=utf-8-*-
# @Time : 2022/4/3 17:30
# @Author:熊金海
# @File : 6.py
# @Software: PyCharm
import os

import requests
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# poj = re.compile(r'.*?src="https://(?P<src>.*?)">',re.S)
#
# url = 'https://www.i6v.cc/e/DownSys/play/?classid=20&id=13804&pathid1=43&bf=0'
# resp = requests.get(url)
#
# url2 = poj.search(resp.text).group("src")
# url2 = "https://"+url2

baseurl = 'https://cc.sssspppp.com/stream/full/japan/4000/FC2PPV-2763643.m3u8'
resp =requests.get(baseurl)

with open("嘿嘿.m3u8",mode="wb") as f:
    f.write(resp.content)
# 解析M3u8文件
n=1
url = 'https://cc.sssspppp.com/stream/full/japan/4000/'
list =[]
with open("嘿嘿.m3u8",mode="r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue
        video_url = url +line
        # print(video_url)

        resp2 = requests.get(video_url)
        f = open(f"video/{n}.ts", mode="wb")
        f.write(resp2.content)
        n += 1
        print("下载一个")
        lis= []
        lis.append(f"video/{n}.ts")
    #
    # s ="+".join(lis)
    # os.system(f"copy /b {s} > movie.mp4")
    # print("搞定！")


'https://cc.sssspppp.com/stream/full/japan/4000/FC2PPV-2763643.ts'
