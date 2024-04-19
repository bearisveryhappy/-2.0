# -*- coding: UTF-8 -*- #
"""
@filename:炸金花.py
@author:Xiong
@time:-02-01
"""
import random


def inp_name():
    names = input("请输入玩家的姓名：")
    name_list = names.split('，')
    return name_list

def ren_puku(name_list):
    nums = 'A23456789JQK'
    flowr_color = ['黑桃','红桃','方片','梅花']
    puke_name = []
    for j in range(len(name_list)*3):
        ran_name = random.choice(flowr_color) + random.choice(nums)
        puke_name.append(ran_name)
    for i in puke_name:
        if i not in puke_name:
            return puke_name
    print(puke_name)
        # else:
            # return puke_name
# def fenpei (name ,puke):
#     dic = {}
#     for i in name:
#         count = 0
#         for j in range(3):
#             dic[i] = puke[0+count:3+count]
#             count += 3
#     return dic

namelist = inp_name()
pukr_name = ren_puku(namelist)
# print(pukr_name)
# finall= fenpei(namelist,pukr_name)
# print(finall)
