class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializes the game settings"""
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (176, 196, 222)
        self.caption = 'Alien Invasion'
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 3
        self.bullet_width = 7
        self.bullet_height = 7
        self.bullet_color = (236, 80, 33)
        self.bullets_allowed = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.ship_limit = 3
