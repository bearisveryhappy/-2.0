# -*-coding=utf-8-*-
# @Time : 2022/4/14 15:31
# @Author:熊金海
# @File : 游戏.py
# @Software: PyCharm
import random
import sys
import pygame
class Ball(object):
    def __int__(self):
        self.ballRect = pygame.Rect(60,50,50,50)
        self.ballDtaus = [pygame.image.load("2.png"),
                          pygame.image.load("3.png"),
                          pygame.image.load("4.png")]
        self.status = 0
        self.ballX=120
        self.ballY= 350
        self.jump=False
        self.jumpSpeed = 10
        self.gravity=5
        self.dead = False


    def ballUpadate(self):
        if self.jump:
            self.jumpSpeed-=1
            self.ballY-=self.jumpSpeed
        else:
            self.gravity+=0.2
            self.ballY+=self.gravity
        self.ballRect[1]=self.ballY



class Pipeline(object):
    def __int__(self):
        self.wallx =400;
        self.pineUp =pygame.image.load("5.png")
        self.pineDown =pygame.image.load("6.png")

    def updatePipeline(self):
        self.wallx -=5
        if self.wallx <-80:
            self.wallx =400
def createMap():
    screen.fill((255,255,255))
    screen.blit(background,(0,0))
    screen.blit(Pipeline.pineUp,(Pipeline.wallx,-300));
    screen.blit(Pipeline.pineDown, (Pipeline.wallx, 500));
    Pipeline.updatePipeline()
    if Ball.dead:
        Ball.status = 2
    elif Ball.jump:
        Ball.status = 1
    screen.blit(Ball.ballStatus[Ball.status],(Ball.ballX,Ball.ballY))
    Ball.ballUpadate()
    pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    size = width,height =400,650
    screen =pygame.display.set_mode(size)
    clock  =pygame.time.Clock()
    Pipeline = Pipeline()
    Ball =Ball()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if (event.type ==pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Ball.dead:
            Ball.jump=True
            Ball.gravity =5
            Ball.jumpSpeed = 10
    background = pygame.image.load("1.png")
    createMap()
