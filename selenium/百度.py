from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os
import csv

filename = "introduce\\"
if not os.path.exists(filename):
    os.mkdir(filename)

info = Service('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
web = webdriver.Edge(service = info)
web.get("https://www.dygang.cc/ys/")

time.sleep(1)

# web.find_element_by_xpath('//*[@id="kw"]').send_keys("学习方法",Keys.ENTER)

# time.sleep(1)
#
# click = web.find_element_by_xpath('//*[@id="2"]/div/div[1]/h3/a').click()

f =open(filename + "1.csv",mode="w")
writerow = csv.writer(f)
list_1 = web.find_elements_by_xpath('/html/body/table[6]/tbody/tr/td[1]/table/tbody/tr/td/table[2]/tbody/tr')
lis = []
for i in list_1:
    name_1 = i.find_element_by_xpath('./td[1]/table/tbody/tr/td[2]/a').text
    name_2 = i.find_element_by_xpath('./td[2]/table/tbody/tr/td[2]/a').text
    intro_1 = i.find_element_by_xpath('./td[1]/table/tbody/tr[2]/td').text
    intro_2 = i.find_element_by_xpath('./td[2]/table/tbody/tr[2]/td').text
    lis.append(name_1)
    lis.append(name_2)
    lis.append(intro_1)
    lis.append(intro_2)
    writerow.writerow([name_1,intro_1,name_2,intro_2])

f.close()

