# -*-codeing=utf-8-*-
# @Time : 2022/3/6 17:38
# @Author:熊金海
# @File : 创建excel文件.py
# @Software: PyCharm
import xlwt

workbook =xlwt.Workbook(encoding="utf-8")
worksheet=workbook.add_sheet('第一张工作表')
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d*%d=%d"%((i+1),(j+1),(i+1)*(j+1)))
workbook.save('第一个excel.xls')