import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:

    def __init__(self):
        """Inicializa el juego y crea los recursos del juego"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Invasion Alienigena")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.bg_color = self.settings.bg_color

    def run_game(self) -> None:
        """Inicia el loop del juego"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self) -> None:
        """Captura los eventos en el loop de ejecucion y los almacena en variables para tomar las decisione de que hacer."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Metodo para ejecutar eventos KEYDOWN segun logica establecida en el hilo de ejecucion principal"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # evento de las teclas cuando dejan de estar presionadas
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Crea una nueva bala"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        # Actualiza posicion de los proyectiles
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= self.settings.bullets_allowed:
                self.bullets.remove(bullet)
                print(len(self.bullets))

    def _update_screen(self):
        """Actualiza la pantalla"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == "__main__":
    # Crea una instancia del juego y ejecuta el juego.
    ai = AlienInvasion()
    ai.run_game()
