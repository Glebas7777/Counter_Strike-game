import pygame
from menu import Menu
from swat import Swat
import shelve
settings = Menu()


def game_settings():
    pygame.init()
    settings_screen = pygame.display.set_mode((700, 800))
    running = True
    settings.append_option('Classic Swat', lambda: print(set_swat(num=1)))
    settings.append_option('Desert Swat', lambda: print(set_swat(num=2)))
    settings.append_option('Winter Swat', lambda: print(set_swat(num=3)))
    settings.append_option('Back', lambda: print(quit()))
    settings.append_option("Continue", lambda: print('run'))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save = Save()
                save.save()
                save.get()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    settings.switch(-1)
                elif event.key == pygame.K_s:
                    settings.switch(1)
                elif event.key == pygame.K_RETURN:
                    settings.select()
        settings_screen.blit(pygame.image.load('images/settings.img.png'), (0, 0, 700, 800))
        settings.draw(settings_screen, 100, 100, 75)
        pygame.display.flip()


def set_swat(num):
   Swat.image = pygame.image.load('images/pixil-frame-(1).png'.format(num))


class Save:
    def __init__(self):
        self.file = shelve.open('data')
        self.info = set_swat(game_settings())

    def save(self):
        self.file['info'] = self.info
        self.file['number'] = 25

    def get(self):
        num = self.file['number']
        print(num)
        print(self.file['info'])

    def __del__(self):
        self.file.close()


save = Save()
