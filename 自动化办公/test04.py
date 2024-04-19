# -*-codeing=utf-8-*-
# @Time : 2022/5/6 14:37
# @Author:熊金海
# @File : test04.py
# @Software: PyCharm
import time
import unittest

from selenium import webbrowser

class TestTshop(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webbrowser.Chrome()
        self.driver.implicity_wait(10)
        self.driver.__getattribute__()