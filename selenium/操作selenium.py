# -*-coding=utf-8-*-
# @Time : 2022/4/29 17:24
# @Author:熊金海
# @File : 操作selenium.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys

import time

s = Service('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
web = webdriver.Edge(service = s)
web.get('https://www.lagou.com')

#找到某个元素，然后点击他
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a').click()

time.sleep(2)  #让浏览器缓一会

#找到输入框，输入内容  回车
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER)

#找到存放的数据的位置，进行数据提取
#找到页面中存放的数据的所有的li

time.sleep(2)

li_list = web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div')
for li in li_list:
    job_name = li.find_element_by_xpath('./div/div/div/a').text
    job_price = li.find_element_by_xpath('./div/div/div[2]/span').text
    company_name = li.find_element_by_xpath('./div/div[2]/div/a').text

    print(company_name,job_name,job_price)



















