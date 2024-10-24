import pygame

import sys

from settings import Settings
from cohete import Cohete


class JuegoCohete:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_widht, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Juego de Cohete")

        self.cohete = Cohete(self)

    def run_game(self):

        while True:

            self._check_events()
            self.cohete.update()
            self._update_screen()
            self.clock.tick(144)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_a:
            self.cohete.moving_left = True
        if event.key == pygame.K_d:
            self.cohete.moving_right = True
        if event.key == pygame.K_w:
            self.cohete.moving_up = True
        if event.key == pygame.K_s:
            self.cohete.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_a:
            self.cohete.moving_left = False
        if event.key == pygame.K_d:
            self.cohete.moving_right = False
        if event.key == pygame.K_w:
            self.cohete.moving_up = False
        if event.key == pygame.K_s:
            self.cohete.moving_down = False

    def _update_screen(self):

        self.cohete.blitme()
        pygame.display.flip()
        self.screen.fill(self.settings.color_bg)


if __name__ == "__main__":

    game = JuegoCohete()
    game.run_game()
