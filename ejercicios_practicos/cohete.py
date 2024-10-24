import pygame


class Cohete:

    def __init__(self, juego_cohete):
        self.screen = juego_cohete.screen
        self.screen_rect = juego_cohete.screen.get_rect()
        self.settings = juego_cohete.settings

        self.image = pygame.image.load("imagen/cohete.jpg")
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.speed
        if self.moving_down and self.rect.bottom < 600:
            self.rect.y += self.settings.speed
