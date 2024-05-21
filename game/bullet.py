import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, swat):
        """создаем пулю в позиции спецназа"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.colour = 219, 193, 219
        self.speed = 4.5
        self.rect.centerx = swat.rect.centerx
        self.rect.top = swat.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
