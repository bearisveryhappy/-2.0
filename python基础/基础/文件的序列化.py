# -*-codeing=utf-8-*-
# @Time : 2022/4/4 11:23
# @Author:熊金海
# @File : 文件的序列化.py
# @Software: PyCharm
import json

# f = open("text.txt","w")
#
# list = [1,23,4,5]
#dumps
# result = json.dumps(list,f)
# f.write(result)
#
# #dump
# json.dump(list,f)
# f.close()
import json
# f = open("text.txt","r")
#
# content = f.read()
#loads
# result = json.loads(content)
# print(type(result))

#load
f = open("text.txt","r")

result = json.load(f)

print(type(result))






























