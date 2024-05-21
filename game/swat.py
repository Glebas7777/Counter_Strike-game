import pygame
from pygame.sprite import Sprite


class Swat(Sprite):

    def __init__(self, screen):
        """иницализация спецназа"""
        super(Swat, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-(1).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """рисование спецназа"""
        self.screen.blit(self.image, self.rect)

    def update_swat(self):
        """обновление позиции спецназа"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.centerx += 1
        if self.mleft and self.rect.left > 0:
            self.centerx -= 1

        self.rect.centerx = self.centerx

    def create_gun(self):
        """размещает спецназа по центру внизу"""
        self.center = self.screen_rect.centerx
