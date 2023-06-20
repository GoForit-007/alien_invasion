#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/6/20 21:07
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理飞船所发射的子弹的类'''
    def __init__(self,ai_game):
        '''在飞船的当前位置创建一个子弹对象'''
        super(Bullet, self).__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color

        # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop

        # 存储用浮点数表示的子弹位置
        self.y=float(self.rect.y)
