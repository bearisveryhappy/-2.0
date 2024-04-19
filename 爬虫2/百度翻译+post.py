# -*-codeing=utf-8-*-
# @Time : 2022/3/25 15:45
# @Author:熊金海
# @File : 百度翻译+post.py
# @Software: PyCharm




import requests

url="https://fanyi.baidu.com/sug"

s=input("输入一个文字：")

dic={
    "kw": s
}

resp=requests.post(url,data=dic)
print(resp.json())





























