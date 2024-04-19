# -*-codeing=utf-8-*-
# @Time : 2022/5/5 14:38
# @Author:熊金海
# @File : test01.py
# @Software: PyCharm
def add (x,y):
    return x+y


import unittest
class TestAdd(unittest.TestCase):
    def test01_add(self):
        result1 = add(0,0)
        print("result ==",result1)

    def test02_add(self):
        result2 = add(1,1)
        print("result ==", result2)
        self.assertEqual(2,result2)