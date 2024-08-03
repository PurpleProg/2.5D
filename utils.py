""" little piece of code to help clarify and simplify the project """
import pygame


class Tile:
    """ container for a basic tile """
    def __init__(self) -> None:
        self.size = 64
        self.color = '#ff0000'
        self.image = pygame.Surface(size=(self.size, self.size))
        self.image.fill(self.color)
        self.rect: pygame.Rect = self.image.get_rect()
