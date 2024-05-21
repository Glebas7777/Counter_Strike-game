import pygame
import sys
from bullet import Bullet
from terrorist import Terrorist
import time
pygame.init()
s = pygame.mixer.Sound('sounds/gromkiy-pistoletnyiy-vyistrel.ogg')
run = pygame.mixer.Sound('sounds/beg-po-betonu-variant-2-25270.ogg')


def events(screen, swat, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                swat.mright = True
                run.play()
            #влево
            elif event.key == pygame.K_a:
                swat.mleft = True
                run.play()
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, swat)
                bullets.add(new_bullet)
                s.play()
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                swat.mright = False
            #влево
            elif event.key == pygame.K_a:
                swat.mleft = False


def update(bg_colour, screen, stats, sc, swat, terrorists, bullets):
    """обновление экрана"""
    screen.fill(bg_colour)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    swat.output()
    terrorists.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, terrorists, bullets):
    """обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, terrorists, True, True)
    if collisions:
        for terrorists in collisions.values():
            stats.score += 10 * len(terrorists)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_swats()
    if len(terrorists) == 0:
        bullets.empty()
        create_army(screen, terrorists)


def swat_kill(stats, screen, sc, swat, terrorists, bullets):
    """столкновение спецназа и армии"""
    if stats.swats_left > 0:
        stats.swats_left -= 1
        terrorists.empty()
        bullets.empty()
        create_army(screen, terrorists)
        swat.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_terrorists(stats, screen, sc, swat, terrorists, bullets):
    """обновляет позицию террористов"""
    terrorists.update()
    if pygame.sprite.spritecollideany(swat, terrorists):
        swat_kill(stats, screen, sc, swat, terrorists, bullets)
    terrorists_check(stats, screen, sc, swat, terrorists, bullets)


def terrorists_check(stats, screen, sc, swat, terrorists, bullets):
    """проверка, добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()
    for terrorist in terrorists.sprites():
        if terrorist.rect.bottom >= screen_rect.bottom:
            swat_kill(stats, screen, sc, swat, terrorists, bullets)
            break


def create_army(screen, terrorists):
    """создание армии террористов"""
    terrorist = Terrorist(screen)
    terrorist_width = terrorist.rect.width
    number_terrorist_x = int((700 - 2 * terrorist_width) / terrorist_width)
    terrorist_height = terrorist.rect.height
    number_terrorist_y = int((800 - 100 - 2 * terrorist_height) / terrorist_height)

    for row_number in range(number_terrorist_y - 1):
        for terrorist_numer in range(number_terrorist_x):
            terrorist = Terrorist(screen)
            terrorist.x = terrorist_width + terrorist_width * terrorist_numer
            terrorist.y = terrorist_height + terrorist_height * row_number
            terrorist.rect.x = terrorist.x
            terrorist.rect.y = terrorist.rect.height + terrorist.rect.height * row_number
            terrorists.add(terrorist)


def check_high_score(stats,sc):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))

