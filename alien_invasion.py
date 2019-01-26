import pygame
import os
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
import game_functions as gf


def run_game():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 100)
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.caption)
    ship = Ship(settings, screen)
    aliens = Group()
    bullets = Group()
    stats = GameStats(settings)
    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(settings, screen, ship, aliens, bullets)
            gf.update_aliens(settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(settings, screen, ship, aliens, bullets)


run_game()
