import pygame.font
from swat import *
from pygame.sprite import Group


class Scores:
    """вывод игровой информации"""
    def __init__(self, screen, stats):
        """инициализируем подсчет очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_colour = (219, 193, 219)
        self.font = pygame.font.SysFont('Arial', 36)
        self.image_score()
        self.image_high_score()
        self.image_swats()

    def image_score(self):
        """преобразовывает текст счета в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_colour, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """преобразует рекорд в графическое изображение"""
        self.high_score_image = self.font.render(str(self.stats.high_score),
                                                 True, self.text_colour, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_swats(self):
        """количество жизней"""
        self.swats = Group()
        for swat_number in range(self.stats.swats_left):
            swat = Swat(self.screen)
            swat.rect.x = 15 + swat_number * swat.rect.width
            swat.rect.y = 20
            self.swats.add(swat)

    def show_score(self):
        """вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.swats.draw(self.screen)
