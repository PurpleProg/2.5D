""" level class """
import math
import pygame
from player import Player
from utils import Tile


class Level:
    """ handle map and raycasting """
    def __init__(self) -> None:
        self.map: list[list[int]] = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        ]
        self.player = Player()
        self.tiles = []

        for y, column in enumerate(self.map):
            for x, wall in enumerate(column):
                if wall:
                    tile = Tile(color='#ff0000')
                else:
                    tile = Tile(color='#121212')
                tile.rect.x = x*tile.size + x
                tile.rect.y = y*tile.size + y
                self.tiles.append(tile)

    def update(self, keys: set) -> None:
        """ update the player """
        self.player.update(keys=keys)

    def cast_ray(self, canvas: pygame.Surface, player) -> None:
        """ draw a line to next wall, use player.angle """

        # avoid undef tangent
        if abs(math.cos(player.angle)) < 1e-10:
            return

        # calc tangent once per frame
        tangent = math.tan(player.angle)

        # get nearest line
        initial_pos_y = round(player.rect.centery / 64) * 64

        # the ray goes max 10 * 64 if no wall are found.
        # this loop should be break in a normal use
        for i in range(11):
            # looking down
            if 0 < player.angle and player.angle < math.pi:
                end_pos_y = initial_pos_y + (64 * i)
                end_pos_x = player.rect.centerx + (tangent * abs(end_pos_y - player.rect.centery))
            # looking up
            elif math.pi < player.angle and player.angle < 2 * math.pi:
                end_pos_y = initial_pos_y - (64 * (i + 1))
                end_pos_x = player.rect.centerx - (tangent * abs(end_pos_y - player.rect.centery))

            # clamp map indexs to map size
            map_index_y = min(int(max(end_pos_y / 64, 0)), len(self.map) - 1)
            map_index_x = min(int(max(end_pos_x, 0) // 64), len(self.map[0]) - 1)

            print(tangent)

            # find collision with walls
            if self.map[map_index_y][map_index_x]:
                break

        pygame.draw.line(
            surface=canvas,
            color='#0000ff',
            start_pos=player.rect.center,
            end_pos=(end_pos_x, end_pos_y)
        )

    def render(self, canvas: pygame.Surface) -> None:
        """ blit tiles to a canvas render player"""
        # blit tiles
        for tile in self.tiles:
            tile.render(canvas=canvas)

        self.cast_ray(canvas=canvas, player=self.player)

        self.player.render(canvas=canvas)
