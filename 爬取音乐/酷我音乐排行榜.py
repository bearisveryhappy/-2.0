# -*-codeing=utf-8-*-
# @Time : 2023/2/14 23:19
# @Author:熊金海
# @File : 酷我音乐排行榜.py
# @Software: PyCharm
import requests
import os
import json

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E8%96%9B%E4%B9%8B%E8%B0%A6',
    'csrf': 'HC5O18GGZ2W',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1650628124; _ga=GA1.2.2003697272.1650628124; _gid=GA1.2.50197960.1650628124; uname3=%u66AE%u51AC; t3kwid=576841680; userid=576841680; websid=1148727894; pic3="https://thirdwx.qlogo.cn/mmopen/vi_32/5zCXL4ibFZ5R4HK4BpCnWM1w627P5S8fkFwcr428RSdsia9HHs5rPkib9CWrLcRicvAIy2RVBUVmMxAGgd5KJtwibGw/132"; t3=weixin; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1650628910; kw_token=HC5O18GGZ2W'
}


for page in range(1,16):
    url= f'http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn={page}&rn=20&httpsStatus=1&reqId=7ec59920-ac7a-11ed-a819-7ba478a5569d'

    result =requests.get(url ,headers=headers).json()
    # print(result)

    filename = '热歌\\'

    if not os.path.exists(filename):
        os.mkdir(filename)

    data = result['data']['musicList']

    for i in data:
        name =i['name']
        rid = i['rid']
        # print(name,rid)
        url2 = f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={rid}&type=music&httpsStatus=1&reqId=c93411c1-c239-11ec-bfe4-bbe6535ee566'
        result2 =requests.get(url2,headers=headers).json()
        # print(result2)

        music_url =result2['data']['url']
        if data == None:
            continue
         # print(music_url)
        else:
            with open(f"{filename}/{name}.mp3","wb") as f :
                print(f"正在下载{name}",end='')
                music = requests.get(music_url)
                f.write(music.content)
                f.close()
                print("\t下载完成！！")