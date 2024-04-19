# -*- coding: UTF-8 -*- #
"""
@filename:替换文件内文字.py
@author:Xiong
@time:-01-31
"""
f = open('D:\作业\python基础\\1.txt',mode="r+",encoding="utf-8")
data = f.read().replace('好天气','坏天气')
f.seek(0)#将光标移动到0位置
f.truncate() #清空文件

f.write(data)
f.close()