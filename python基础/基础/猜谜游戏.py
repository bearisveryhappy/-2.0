# -*-codeing=utf-8-*-
# @Time : 2022/4/14 13:14
# @Author:熊金海
# @File : 猜谜游戏.py
# @Software: PyCharm
import random
import string

# mi = random.randint(1, 100)
mn = string.printable
# mm = string.ascii_uppercase
# mk = string.ascii_lowercase
print(mn)
# print("退出游戏请输入 '0'")
# num = 0
# while True:
#     num+=1
#     num1 = int(input("请输入一个数字："))
#     if num1 != 0 and num1 > mi:
#         print("您输入的数字过大啦！！！")
#     elif num1 != 0 and num1 < mi:
#         print("你输入的数字过小啦！！！")
#     elif num1 != 0 and num1 == mi:
#         print("恭喜你，你猜中了了！！！")
#         print(f"本次游戏共用了{num}次")
#         break
#     elif num1 == 0:
#         endnum = input("你去决定要退出吗？ 输出yes/no  :")
#         if endnum == 'yes':
#             print("退出游戏啦，下次一定要在一起玩哦。")
#             break
