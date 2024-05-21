
import pygame
import choosing
from swat import Swat
import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from menu import Menu
from choosing import *
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
menu = Menu()
menu_screen = pygame.display.set_mode((700, 800))


def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800)) 
    pygame.display.set_caption("Counter-Strike90")
    bg_colour = (0, 0, 0)
    swat = Swat(screen)
    bullets = Group()
    terrorists = Group()
    controls.create_army(screen, terrorists)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, swat, bullets)
        if stats.run_game:
            swat.update_swat()
            controls.update(bg_colour, screen, stats, sc, swat, terrorists, bullets)
            controls.update_bullets(screen, stats,  sc, terrorists, bullets)
            controls.update_terrorists(stats, screen, sc, swat, terrorists, bullets)


menu.append_option('Start', lambda: print(run()))
menu.append_option('Quit', quit)
menu.append_option('Settings', lambda: print(choosing.game_settings()))
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                menu.switch(-1)
            elif e.key == pygame.K_s:
                menu.switch(1)
            elif e.key == pygame.K_RETURN:
                menu.select()

    menu_screen.blit(pygame.image.load('images/menu.png'), (0, 0, 700, 800))
    menu.draw(menu_screen, 100, 100, 75)
    pygame.display.flip()
quit()
