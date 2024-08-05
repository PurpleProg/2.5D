""" player class """
import math
import pygame
import settings


class Player:
    """ player, used to posision the camera """
    def __init__(self) -> None:
        self.image = pygame.Surface(size=(settings.PLAYER_SIZE, settings.PLAYER_SIZE))
        self.image.fill(settings.PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

        self.speed = settings.PLAYER_SPEED
        self.direction = pygame.Vector2(0, 0)   # this is only used for moving

        self.angle = 3 * (math.pi / 2) + 0.5 # in radian this is used for raycast

    def update(self, keys: set) -> None:
        """" move the player and change angle"""
        if 'RIGHT' in keys:
            self.direction.x = 1
        elif "LEFT" in keys:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if 'UP' in keys:
            self.direction.y = -1
        elif 'DOWN' in keys:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if self.direction.length():
            self.direction.normalize_ip()

        self.rect.x += self.speed * self.direction.x
        self.rect.y += self.speed * self.direction.y

        # angle
        if 'a' in keys:
            self.angle -= 0.05
        elif 'd' in keys:
            self.angle += 0.05

        # normalize angle
        if self.angle <= 0:
            self.angle += 2 * math.pi
        elif self.angle >= 2 * math.pi:
            self.angle -= 2 * math.pi

    def render(self, canvas: pygame.Surface) -> None:
        """ draw player to screen """
        canvas.blit(self.image, self.rect)
