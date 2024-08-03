""" level class """
import pygame
from utils import Tile


class Level:
    """ handle map and raycasting """
    def __init__(self) -> None:
        self.map: list[list[bool]] = [
            [1, 1, 1, 1, 1,],
            [1, 0, 0, 0, 0,],
            [1, 0, 1, 1, 1,],
            [1, 0, 0, 0, 0,],
            [1, 1, 1, 1, 1,],
        ]
        self.tile_size = 16

    def update(self) -> None:
        pass

    def render(self, canvas: pygame.Surface) -> None:
        """ blit tiles to a canvas """
        for y, column in enumerate(self.map):
            for x, wall in enumerate(column):
                if wall:
                    tile = Tile()
                    canvas.blit(
                        source=tile.image,
                        dest=(
                            x*tile.size + 100,
                            y*tile.size + 100,
                        )
                    )
