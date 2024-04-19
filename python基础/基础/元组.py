# -*-codeing=utf-8-*-
# @Time : 2022/4/4 9:49
# @Author:熊金海
# @File : 元组.py
# @Software: PyCharm

dic = {
    'name':[1,2,3,4],
    'age':'20'
}

#增
# dic['school'] = '南昌大学'
# print(dic)

#删
# del dic['name']
# print(dic)

# dic.clear()
# print(dic)

#改
# dic ['name'] = '老刘'
# print(dic)

#查
# print(dic['name'])

# print(dic.get('name'))

#遍历所有字典

# for key in dic.keys():
    # print(key)

# for value in dic.values():
#     print(value)
#
for key,value in dic.items():
    print(key,value)

# for item in dic.items():
#     print(list(item))




























