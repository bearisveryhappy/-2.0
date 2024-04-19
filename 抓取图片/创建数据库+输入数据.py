import requests
import re
import json
import pymysql


# 获取html网页内容
def getHTMLText(url, headers):
    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


# 获取json文件内容
def getJson(url, headers):
    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


def insertDB(ID, dateId, provinceShortName, confirmedIncr, curedIncr, deadIncr, currentConfirmedCount, confirmedCount,
             curedCount, deadCount):
    # 插入数据
    try:
        sql = "insert into proday values (%s,'%s','%s',%s,%s,%s,%s,%s,%s,%s)" % (
        ID, dateId, provinceShortName, confirmedIncr, curedIncr, deadIncr, currentConfirmedCount, confirmedCount,
        curedCount, deadCount)
        cursor.execute(sql)
        db.commit()

    except Exception as e:
        db.rollback()
        print(e)


def insertDB2(dateId):
    # 插入数据
    try:
        sql = "insert into a values ('%s')" % (dateId)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)


if __name__ == '__main__':
    # 获取网页源代码
    url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}
    html = getHTMLText(url, headers)

    # 解析网页内容
    reg = '<script id="getAreaStat">([^<]+)'
    china_pro = json.loads(re.findall(reg, html)[0][27:-11])

    # 数据写入数据库
    # 连接数据库
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='data', charset='utf8')
    cursor = db.cursor()
    id = 1
    for pro in china_pro:
        # 省或区
        provinceShortName = pro["provinceShortName"]
        # 各省或区疫情数据
        json_url = pro["statisticsData"]
        json_content = getJson(json_url, headers)
        for day in range(-1, -32, -1):
            data = json.loads(json_content)["data"][day]
            # 日期，省或区，当日新增确诊
            # 当日新增治愈，当日新增死亡,现有确诊人数
            # 累计确诊人数，累计治愈人数，累计死亡人数
            insertDB(id, data["dateId"], provinceShortName, data["confirmedIncr"], data["curedIncr"], data["deadIncr"],
                     data["currentConfirmedCount"], data["confirmedCount"], data["curedCount"], data["deadCount"])
            id = id + 1
    # 关闭数据库
    cursor.close()
    db.close()