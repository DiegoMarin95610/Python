class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Velocidad de la nave
        self.ship_speed = 2.0

        # Configuraciones de municion
        self.bullet_speed = 0.7
        self.bullet_width = 3
        self.bullet_height = 7
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
