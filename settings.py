#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/6/20 19:41
class Settings:
    '''
    存储游戏《外星人》入侵中所有设置的类
    '''

    def __init__(self):
        '''
        初始化游戏的设置
        '''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 外星人速度设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
