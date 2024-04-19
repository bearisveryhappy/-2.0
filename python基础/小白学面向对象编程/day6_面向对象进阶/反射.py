
class Person():
    def __init__(self ,name ,age):
        self.name = name
        self.age = age

    def walk(self):
        print("walking....")

def talk(self):
    print(self.name ,"is speaking.....")

p = Person("Alex" ,22)
if hasattr(p,"name"): # 映射
    print("l.......")


# #反射、映射、自省
# getattr() get
#     a = getattr(p,"age")
#     print(a)

# hasattr()
    # user_command = input(">>:").strip()
    # if hasattr(p,user_command):
    #     func = getattr(p,user_command)
    #     func()

# setattr()  赋值
#     ## static 属性
#     setattr(p,"sex","Female")
#     print(p.sex)
#     ## 方法
#
#     # setattr(p,"speak",talk)
#     # p.speak(p)
#
#     setattr(Person,"speak2",talk)
#
#     p.speak2()

# delattr()

#delattr(p,"age")
# del p.age
# p.age

#getattr("反射.py","p")

# print(__name__) # __main__ 就代表模块本身， self.
#
# if __name__ == "__main__": #只会在被别的模块导入的时候发挥作用
#     print("hahahah")
#
# #print('hahaha')

#
# import sys
# # for k,v in sys.modules.items():
# #     print(k,v)
#
# #print(sys.modules["__main__"])
# mod = sys.modules[__name__]
# if hasattr(mod,"p"):
#     o = getattr(mod,"p")
#     print(o)
# print(p)
#
# #import "os"

class User:
    def login(self):
        print('欢迎来到登录页面')
    def register(self):
        print('欢迎来到注册页面')
    def save(self):
        print('欢迎来到存储页面')

u = User()
while True:
    user_cmd = input(">>:").strip()
    if hasattr(u,user_cmd):
        func = getattr(u,user_cmd)
        func()