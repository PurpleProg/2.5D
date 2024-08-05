""" little piece of code to help clarify and simplify the project """
import math
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


def draw_line(
    canvas: pygame.Surface,
    start_pos: tuple[int, int],
    lengh: int,
    angle: float,
    color,
    width: int=1
    ) -> None:
    """ draw a line from a size and a angle in radians """
    # i hate trigonometry
    end_pos_x = start_pos[0] + (math.cos(angle) * lengh)
    end_pos_y = start_pos[1] + (math.sin(angle) * lengh)
    pygame.draw.line(
            surface=canvas,
            start_pos=start_pos,
            end_pos=(
                end_pos_x,
                end_pos_y
            ),
            color=color,
            width=width
        )
