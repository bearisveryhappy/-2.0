# -*-codeing=utf-8-*-
# @Time : 2022/4/4 10:54
# @Author:熊金海
# @File : 读写文件.py
# @Software: PyCharm
#创建文件
import csv

f = open("../爬虫/text.txt","w")
f.write("今天甜腻去不错\n" * 10)
#
# #读文件
#
# f = open("../爬虫/text.txt","r")
# content = f.read()
# print(content)


# f = open("../爬虫/text.txt","r")
# content = f.readlines()
# print(content)


#创建一个csv文件

# f = open("../爬虫/csv.txt","w")
# csvwriter=csv.writer(f)
#
# csvwriter.writerow("你好啊！！！")



#创建一个excel文件

# import xlwt
#
# workbook =xlwt.Workbook(encoding="utf-8")
# worksheet=workbook.add_sheet('第一张工作表',cell_overwrite_ok=True)
# worksheet.write(0,0,"今天天气非常好！！")
# workbook.save('第一个excel.xls')










































