""" little piece of code to help clarify and simplify the project """
import pygame
import settings


class Tile:
    """ container for a basic tile """
    def __init__(self, color) -> None:
        self.size = settings.TILE_SIZE - settings.GRID_GAP
        self.color = color
        self.image = pygame.Surface(size=(self.size, self.size))
        self.image.fill(self.color)
        self.rect: pygame.Rect = self.image.get_rect()

    def render(self, canvas: pygame.Surface) -> None:
        """ blit """
        canvas.blit(
                source=self.image,
                dest=self.rect
            )
