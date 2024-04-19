# -*-codeing=utf-8-*-
# @Time : 2022/5/13 14:44
# @Author:熊金海
# @File : test07.py
# @Software: PyCharm
import unittest

from htmltestreport import HTMLTestReport
from 自动化操作.test01 import TestAdd
from 自动化操作.test02 import TestSub

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSub))


file_path = "./自动化操作/report.html"
report = HTMLTestReport(file_path,title = "Web自动化测试报告",description="win10...")
report.run(suite)
