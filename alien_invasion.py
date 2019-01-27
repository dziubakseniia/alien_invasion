import pygame
import os
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 100)
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.caption)
    play_button = Button(settings, screen, "Play")
    ship = Ship(settings, screen)
    aliens = Group()
    bullets = Group()
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, stats, play_button, ship, aliens,
                        bullets)

        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(settings, screen, ship, aliens, bullets)
            gf.update_aliens(settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
