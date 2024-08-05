""" player class """
import math
import pygame
import settings


class Player:
    """ player, used to posision the camera """
    def __init__(self) -> None:
        self.image = pygame.Surface(size=(settings.PLAYER_SIZE, settings.PLAYER_SIZE))
        self.image.fill(settings.PLAYER_COLOR)
        # i wont refractor all the raycaster self.rect is a Frect
        self.rect: pygame.FRect = self.image.get_frect()
        self.rect.x = 128.0
        self.rect.y = 128.0

        self.speed = settings.PLAYER_SPEED

        self.angle = 3 * (math.pi / 2) + 0.5 # in radian this is used for raycast

    def update(self, keys: set) -> None:
        """" move the player and change angle"""

        # move player
        if 'UP' in keys:
            self.rect.x += math.cos(self.angle) * self.speed
            self.rect.y += math.sin(self.angle) * self.speed
        elif 'DOWN' in keys:
            self.rect.x += math.cos(self.angle + math.pi) * self.speed
            self.rect.y += math.sin(self.angle + math.pi) * self.speed
        if 'a' in keys:
            self.rect.x += math.cos(self.angle - (math.pi/2)) * self.speed
            self.rect.y += math.sin(self.angle - (math.pi/2)) * self.speed
        elif 'd' in keys:
            self.rect.x += math.cos(self.angle + (math.pi/2)) * self.speed
            self.rect.y += math.sin(self.angle + (math.pi/2)) * self.speed

        # change angle
        if 'RIGHT' in keys:
            self.angle += 0.05
        elif 'LEFT' in keys:
            self.angle -= 0.05

    def render(self, canvas: pygame.Surface) -> None:
        """ draw player to screen """
        canvas.blit(self.image, self.rect)
