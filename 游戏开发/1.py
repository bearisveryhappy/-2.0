# -*-codeing=utf-8-*-
# @Time : 2022/4/14 15:59
# @Author:熊金海
# @File : 爬取新发地.py
# @Software: PyCharm

import sys
import pygame
pygame.init()
#显示框
size=width,height=1000,1000
screen=pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()