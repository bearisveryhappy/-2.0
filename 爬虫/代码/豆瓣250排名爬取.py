# -*-codeing=utf-8-*-
# @Time : 2022/3/6 11:54
# @Author:熊金海
# @File : 豆瓣250排名爬取.py
# @Software: PyCharm
# -*-codeing=utf-8-*-
# @Time : 2022/3/5 12:39
# @Author:熊金海
# @File : 电影港爬取.py
# @Software: PyCharm


import re
from io import BytesIO
from bs4 import BeautifulSoup
import urllib.request,urllib.error
import xlwt
import sqlite3



def main():
    baseurl = "https://movie.douban.com/top250?start="
    #爬取网页
    datalist = getData(baseurl)
    savepath = "./豆瓣250.xls"
    saveData(datalist,savepath)

    #askURL("https://movie.douban.com/top250?start=")

#影片详情链接的规则
findLink=re.compile(r'<a href="(.*?)">',re.S)  #创建正则表达式对象，表示规则（字符串模式）
#影片图片的链接
findImgSrc =re.compile(r'<img.*src="(.*?)"',re.S)  #re.S 让换行符包含在字符里面
#影片的片名
findTitle =re.compile(r'<span class="title">(.*?)</span>',re.S)
#影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq=re.compile(r'<span class="inq">(.*?)</span>',re.S)
#找到影片的相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)


# 爬取页面
def getData(baseurl):
    datalist = []
    for i in range(10):  # 调用获取页面信息的函数，10次
        url = baseurl+str(i*25)
        html = askURL(url)  # 保存获取到的网页源码

        # 逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            # print(item)  #测试，查看电影item全部信息
            data = []  # 保存一部电影的所有信息
            item = str(item)  # 类型转换

            # #影片的详情链接
            link=re.findall(findLink,item)[0]   #re库用来通过正则表达式查找指定字符串
            data.append(link)                      #添加链接
            # print(data)

            imgSrc=re.findall(findImgSrc,item)[0]
            data.append(imgSrc)                 #添加图片

            titles=re.findall(findTitle,item)   #片名可能只有一个中文名，没有外国名
            if(len(titles)==2):
                ctitle = titles[0]              #添加中文名
                data.append(ctitle)
                otitle=titles[1].replace('/','')    #去掉无关符号,把 / 替换成空格
                data.append(otitle)             #添加外国名
            else:
                data.append(titles[0])
                data.append(' ')        #外国名字留空

            rating=re.findall(findRating,item)[0]
            data.append(rating)#添加评分

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)#添加评价人数

            inq = re.findall(findInq,item)
            if len(inq) !=0:
                inq = inq[0].replace('。','')#去掉 。
                data.append(inq)        #添加概述
            else:
                data.append(" ")  #留空

            bd =re.findall(findBd,item)[0]
            bd =re.sub('<br(\s+)?/>(\s+)?'," ",bd)       #去掉<br/>
            bd =re.sub("/"," ",bd)  #替换
            data.append(bd.strip())#去掉前后的空格

            datalist.append(data)   #把处理好的一部电影信息放入datalist
    return datalist


# 得到一个指定的url的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
    }

    # 封装                                 #携带者头部信息访问url
    request = urllib.request.Request(url, headers=head)
    html = ""  # 存储
    try:
        # 接受封装对象                     #包含 url 头部信息
        response = urllib.request.urlopen(request)  # response 保存网页信息
        html = response.read().decode('utf-8')  # 读取网页用read
        #print(html)
    except urllib.error.URLError as e:  # 捕获错误信息
        if hasattr(e, "code"):  # 保存出现的问题
            print(e.code)
        if hasattr(e, "reason"):  # 没有捕获成功原因
            print(e.reason)
    return html


# file=open("./saveData","rb")
# html2=file.read()
# bs=BeautifulSoup(html2,"html2,parser")
# print(bs.titie)

# 保存信息
def saveData(datalist,savepath):
    # print("save")
    workbook = xlwt.Workbook(encoding="utf-8")
    sheet = workbook.add_sheet('豆瓣排名250.xlsx',cell_overwrite_ok=True)#覆盖原单元格信息
    col=("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])  #列名
    for i in range(0,250):
        print("第%d条"%i)
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])#数据#第一行参数 “行” ，第二行参数 “列”，第三个参数 “内容”    workbook.save('豆瓣250.xls')

    workbook.save(savepath)




if __name__ == "__main__":
    main()