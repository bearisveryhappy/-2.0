# -*-codeing=utf-8-*-
# @Time : 2023/2/15 0:15
# @Author:熊金海
# @File : 合成视频.py
# @Software: PyCharm
with open("西游记/01.mp4", "wb") as f:
    with open("西游记/end.txt", "r") as f1:
        t = 000
        for line in f1:
            if line.startswith("#"):
                continue
            line = line.strip()
            with open("西游记/video/{}.ts".format(t), "rb") as f2:
                f.write(f2.read())
                t += 1