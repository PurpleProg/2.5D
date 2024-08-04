""" little piece of code to help clarify and simplify the project """
import pygame
import math


class Tile:
    """ container for a basic tile """
    def __init__(self) -> None:
        self.size = 64
        self.color = '#ff0000'
        self.image = pygame.Surface(size=(self.size, self.size))
        self.image.fill(self.color)
        self.rect: pygame.Rect = self.image.get_rect()


def draw_line(
    canvas: pygame.Surface,
    start_pos: tuple[int, int],
    lengh: int,
    angle: int,
    color
    ) -> None:
    """ draw a line from a size and a angle in degres """
    # i hate trigonometry
    end_pos_x = start_pos[0] + (math.cos(math.radians(angle)) * lengh)
    end_pos_y = start_pos[1] + (math.sin(math.radians(angle)) * lengh)
    pygame.draw.line(
            surface=canvas,
            start_pos=start_pos,
            end_pos=(
                end_pos_x,
                end_pos_y
            ),
            color=color
        )
