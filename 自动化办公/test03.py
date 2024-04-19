# -*-codeing=utf-8-*-
# @Time : 2022/5/5 15:09
# @Author:熊金海
# @File : test03.py
# @Software: PyCharm
import unittest
from test01 import TestAdd

from test02 import TestSub

suite = unittest.TestSuite()

suite.addTest(TestAdd("test01_add"))
suite.addTest(unittest.makeSuite(TestSub))

unittest.TextTestRunner().run(suite)
