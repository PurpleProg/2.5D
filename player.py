""" player class """
import pygame


class Player:
    """ player, used to posision the camera """
    def __init__(self) -> None:
        self.image = pygame.Surface(size=(16, 16))
        self.image.fill('#ff0000')
        self.rect = self.image.get_rect()

        self.speed = 10
        self.direction = pygame.Vector2(0, 0)

    def update(self, keys: set) -> None:
        """" move the player """
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

    def render(self, canvas: pygame.Surface) -> None:
        """ draw player to screen """
        canvas.blit(self.image, self.rect)