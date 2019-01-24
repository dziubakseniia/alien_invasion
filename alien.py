import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (50, 63))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x = self.settings.alien_speed_factor
        self.rect.x += (self.settings.alien_speed_factor *
                        self.settings.fleet_direction)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
