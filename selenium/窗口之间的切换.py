# -*-codeing=utf-8-*-
# @Time : 2022/4/29 18:53
# @Author:熊金海
# @File : 窗口之间的切换.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys

import time

s = Service('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
web = webdriver.Edge(service = s)
# web.get('https://www.lagou.com')
#
# el = web.find_element_by_xpath('//*[@id="cboxClose"]').click()
#
# time.sleep(1)
#
# li_list = web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div')
# time.sleep(1)
#
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER)
#
# web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[2]/div[1]/div[1]/div[1]/a').click()
#
# web.switch_to.window(web.window_handles[-1])#切换窗口
#
# job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
#
# #关闭子窗口
# web.close()
# #回到原来的窗口
# web.switch_to.window(web.window_handles[0])

#处理页面遇到iframe的话，必须先拿到iframe，然后再切换视角到iframe，再然后才可以拿数据
web.get('')
iframe = web.find_element_by_xpath('')

web.switch_to.frame(iframe) #进入iframe页面

web.switch_to.default_content()#切换到原页面


