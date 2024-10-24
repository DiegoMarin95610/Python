import pygame


class Ship:
    def __init__(self, ai_game):
        """inicializa la imagen y establece su tamaño."""

        # Captura los datos de la ventana principal, para poder hacer los calculos de la posicion del objeto a agregar.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # carga la imagen y establece su rectangulo de colision.
        self.image = pygame.image.load("images/ship.png")
        self.image = pygame.transform.scale(self.image, (60, 48))
        self.rect = self.image.get_rect()

        # Inicializa la nave espacial en la mitad inferior de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Captura la posicion actual en el eje x de la imagen
        self.x = float(self.rect.x)

        # Define 2 variables en falso, para luego pasarlas al eventon KEYDOWN, que los pone en True mientras el evento KEYDOWN esta activo
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Controla el movimiento de la imagen dentro de la pantalla

        # controla el movimiento en eje x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
