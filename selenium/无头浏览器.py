# -*-codeing=utf-8-*-
# @Time : 2022/4/29 19:40
# @Author:熊金海
# @File : 无头浏览器.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select

import time


# 准备参数配置
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable--gpu")

s = Service('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
web = webdriver.Edge(service = s,options=opt)
web.get('https://ys.endata.cn/BoxOffice/Overseas')
time.sleep(2)

# cli = web.find_element_by_xpath('//*[@id="app"]/section/main/div/div[1]/div/section/section/div/div[1]/div/div/input').click()
# #定位到下拉列表中
# sel_le= web.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul')
# #对元素进行包装，包装成下拉列表
# sel  = Select(sel_le)
# #让浏览器进行调整选项
# for i in range(len(sel.options)): #i 就是每一个下拉框的选项的索引
#     sel.select_by_index(i)  #按照索引进行切换
#     time.sleep(2)
#     table = web.find_element_by_xpath('//*[@id="app"]/section/main/div/div[1]/div/section/section/section/div[1]')
#     print(table.text)
#
# web.close()
#如何拿到页面代码Elements(经过数据加载以及js执行之后的结果的html的内容)
print(web.page_source)



