import pygame


class Ship:

    def __init__(self, settings,  screen):
        self.screen = screen

        self.image = pygame.image.load('images/rocket.png')
        self.image = pygame.transform.scale(self.image, (75, 90))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.settings = settings

        self.center = float(self.rect.centerx)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
