# -*-codeing=utf-8-*-
# @Time : 2022/3/6 18:18
# @Author:熊金海
# @File : 词条摘要.py
# @Software: PyCharm
import requests
from lxml import etree
import json


def request_get(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',

        'Referer':'https://www.liepin.com/zhaopin/?headId=00c1052696958cba62dcd788cc2c5e6e&ckId=fyqc6tj2e70m742wywsw7dtdfxdjfu08&oldCkId=00c1052696958cba62dcd788cc2c5e6e&fkId=dwe2k0nukpco9rrq9adoxqlffk7y3tx8&skId=dwe2k0nukpco9rrq9adoxqlffk7y3tx8&sfrom=search_job_pc&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&currentPage=0&scene=page'
    }
    req=requests.get(url,headers=headers)
    req.encoding=req.apparent_encoding
    return req
def mian_page(text):
    tree=etree.HTML(text)
    li_list=tree.xpath('/html/body/div/div/div/div/ul/li/div/div/div/div/a /')
    for li in li_list:
        name=li.xpath('./div/a/text()')
        urls=li.xpath('./div/a/@href')
        for i,n in zip(urls,name):
            url='https://baike.baidu.com'+i
            url_list.append(url)
            name_list.append(n)
def son_page(text):
    tree=etree.HTML(text)
    # // *[ @ id = "posterCon"] / dd[2] / div / div
    texts=tree.xpath('/html/body/div[3]/div[2]/div/div[1]/div[4]/div//text()')
    if texts==[]:
        texts=tree.xpath('//*[@id ="posterCon"]/dd[2]/div/div//text()')
    a=[x.strip() for x in texts]
    new_texts=''.join(a)
    text_list.append(new_texts)
    for name,url,text in zip(name_list,url_list,text_list):
        jsons={'词条名':'','词条url':'','词条摘要':''}
        jsons['词条名']=name
        jsons['词条url']=url
        jsons['词条摘要']=text
    write_file_json(jsons)
def write_file_json(jsons):
    with open('百度百科.json','a+',encoding='utf-8')as f:
        json.dump(jsons,f,indent=2, sort_keys=True, ensure_ascii=False)
if __name__ == '__main__':
    url_list=[]
    name_list=[]
    text_list=[]
    key=input('请输入关键字:')
    url='https://baike.baidu.com/item/%s'%key
    req=request_get(url).text
    mian_page(req)
    for url in url_list:
        # print(url)
        req=request_get(url).text
        son_page(req)
