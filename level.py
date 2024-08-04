""" level class """
import pygame
from utils import Tile, draw_line
from player import Player


class Level:
    """ handle map and raycasting """
    def __init__(self) -> None:
        self.map: list[list[bool]] = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
            [1, 0, 0, 0, 0,],
            [1, 0, 0, 0, 0, 0, 0, 0,  1, 1, 1,],
            [1, 0, 0, 0, 0,],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0,],
            [1, 0, 0, 0, 0,],
            [1, 0, 0, 0, 0,],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        ]
        self.tile_size = 16
        self.player = Player()

    def update(self, keys: set) -> None:
        """ update the player """
        self.player.update(keys=keys)

    def render(self, canvas: pygame.Surface) -> None:
        """ blit tiles to a canvas and cast rays"""
        for y, column in enumerate(self.map):
            for x, wall in enumerate(column):
                if wall:
                    tile = Tile()
                    canvas.blit(
                        source=tile.image,
                        dest=(
                            x*tile.size,
                            y*tile.size,
                        )
                    )

        # draw lines
        for angle in range(360):
            draw_line(
                canvas=canvas,
                start_pos=self.player.rect.center,
                lengh=300,
                angle=angle,
                color='#0000ff'
            )
