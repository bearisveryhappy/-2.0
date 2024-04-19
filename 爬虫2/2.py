# -*-codeing=utf-8-*-
# @Time : 2022/3/30 15:12
# @Author:熊金海
# @File : 2.py
# @Software: PyCharm

from threading import  Thread


# def func ():
#     for i in range(1000):
#         print("fun",i)
#
# if __name__ == '__main__':
#     t = Thread(target=func)
#     t.start()
#
#     for i in range(1000):
#         print("main",i)
#
# class Mytread(Thread):
#     def run(self):
#         for i in range(1000):
#             print("子线程",i)
#
#
# if __name__ == '__main__':
#     t = Mytread()
#     t.start()
#     for i in range(1000):
#         print("主线程",i)



def func (name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    t1= Thread(target=func,args=("周杰润",))#给线程起名字，传递参数必须是元组
    t1.start()

    t2= Thread(target=func,args=("王力宏",))
    t2.start()
