#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/6/20 18:28
import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    '''
    管理游戏资源和行为的类
    '''

    def __init__(self):
        '''
        初始化游戏并创建游戏资源
        '''
        pygame.init()  # 使用pygame之前必须初始化
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # 设置主屏幕窗口

        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)  # 设置全屏幕窗口
        # self.settings.screen_width=self.screen.get_rect().width
        # self.settings.screen_height=self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")  # 设置窗口的标题，即游戏名称

        self.ship = Ship(self)

    def run_game(self):
        '''
        开始游戏的主循环
        :return:
        '''
        while True:
            # 侦听键盘和鼠标事件
            self._check_events()
            self.ship.update()
            # 每次循环时都重绘屏幕
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        '''
        响应按键和鼠标事件
        :return:
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        '''
        响应按下
        :param event:
        :return:
        '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key==pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        '''
        响应释放
        '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _update_screen(self):
        '''
        更新屏幕上的图像，并切换到新屏幕
        :return:
        '''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
