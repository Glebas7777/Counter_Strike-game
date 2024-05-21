import pygame


class Terrorist(pygame.sprite.Sprite):
    """класс одного террориста"""

    def __init__(self, screen):
        """иницализируем и задаем начальную позицию"""
        super(Terrorist, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (1).png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод террориста на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещает террористов"""
        self.y += 0.1
        self.rect.y = self.y
