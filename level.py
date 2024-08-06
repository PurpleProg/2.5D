""" level class """
import math
import pygame
from player import Player
import settings


class Level:
    """ handle map and raycasting """
    # pylint: disable=C0301
    def __init__(self) -> None:
        self.map_empty: list[list[int]] = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        ]
        self.map_little: list[list[int]] = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        ]
        self.map_wall_all_around: list[list[int]] = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        ]
        self.map_3: list[list[int]] = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]


        self.map = self.map_3

        self.player = Player()
        self.tiles = []

        # create tiles for 2D rendering only
        for y, column in enumerate(self.map):
            for x, wall in enumerate(column):
                if wall:
                    tile = Tile(color=settings.TILE_COLOR)
                else:
                    tile = Tile(color=settings.TILE_BACKGROUND_COLOR)
                tile.rect.x = x*tile.size + x
                tile.rect.y = y*tile.size + y
                self.tiles.append(tile)

    def update(self, keys: set) -> None:
        """ update the player """
        self.player.update(keys=keys)

    def cast_ray(self, player, angle) -> tuple[int, int, str]:
        """ draw a line to next wall, use player.angle """

        angle = self.normalize_angle(angle=angle)

        # calc tangent
        try:
            invert_tangent = 1/math.tan(angle)
        except ZeroDivisionError:
            invert_tangent = 0

        # vertical rays
        for i in range(settings.RAY_MIN_DISTANCE, settings.MAX_RAY_DISTANCE):
            # looking down
            if 0 < angle < math.pi:
                initial_pos_y = math.ceil(player.rect.centery / settings.TILE_SIZE) * settings.TILE_SIZE

                vertical_end_pos_y = initial_pos_y + (settings.TILE_SIZE * i)
                vertical_end_pos_x = player.rect.centerx + (
                    invert_tangent * abs(vertical_end_pos_y - player.rect.centery)
                )
                # clamp map indexs to map size
                map_index_y = min(
                    int(max(vertical_end_pos_y / settings.TILE_SIZE, 0)),
                    len(self.map) - 1
                )
                map_index_x = min(
                    int(max(vertical_end_pos_x / settings.TILE_SIZE, 0)),
                    len(self.map[0]) - 1
                )
            # looking up
            elif math.pi < angle < 2 * math.pi:
                initial_pos_y = math.floor(player.rect.centery / settings.TILE_SIZE) * settings.TILE_SIZE

                vertical_end_pos_y = initial_pos_y - (settings.TILE_SIZE * i)
                vertical_end_pos_x = player.rect.centerx - (
                    invert_tangent * abs(vertical_end_pos_y - player.rect.centery)
                )
                # clamp map indexs to map size
                map_index_y = min(
                    int(max(vertical_end_pos_y / settings.TILE_SIZE, 0)),
                    len(self.map) - 1
                ) -1
                map_index_x = min(
                    int(max(vertical_end_pos_x / settings.TILE_SIZE, 0)),
                    len(self.map[0]) - 1
                )
            # looking strait to the sides
            else:
                # left
                if angle == math.pi:
                    vertical_end_pos_y = player.rect.centery
                    vertical_end_pos_x = 0
                    # print(angle)
                # right
                elif angle == 0:
                    vertical_end_pos_y = player.rect.centery
                    vertical_end_pos_x = settings.WIDTH
                else:
                    raise ValueError(f'unhandle angle : {angle}')
                # clamp map indexs to map size
                map_index_y = min(
                    int(max(vertical_end_pos_y / settings.TILE_SIZE, 0)),
                    len(self.map) - 1
                )
                map_index_x = min(
                    int(max(vertical_end_pos_x / settings.TILE_SIZE, 0)),
                    len(self.map[0]) - 1
                )

            # get the ray lengh (pytagore)
            vertical_lengh = (
                (abs(player.rect.x - vertical_end_pos_x) ** 2) +
                (abs(player.rect.y - vertical_end_pos_y) ** 2)
            )

            # find collision with walls
            if self.map[map_index_y][map_index_x]:
                break

        # calc tangent
        try:
            tangent = math.tan(angle)
        except ZeroDivisionError:
            tangent = 0

        # horizontal rays
        for i in range(settings.RAY_MIN_DISTANCE, settings.MAX_RAY_DISTANCE):
            # looking right
            if 3 * (math.pi / 2) < angle or angle < math.pi / 2:
                # get nearest line
                initial_pos_x = math.ceil(player.rect.centerx / settings.TILE_SIZE) * settings.TILE_SIZE

                horizontal_end_pos_x = initial_pos_x + (settings.TILE_SIZE * i)
                horizontal_end_pos_y = player.rect.centery + (
                    tangent * abs(horizontal_end_pos_x - player.rect.centerx)
                )
                # clamp map indexs to map size
                map_index_x = min(
                    int(max(horizontal_end_pos_x / settings.TILE_SIZE, 0)),
                    len(self.map[0]) - 1
                )
                map_index_y = min(
                    int(max(horizontal_end_pos_y / settings.TILE_SIZE, 0)),
                    len(self.map) - 1
                )
            # looking left
            elif math.pi / 2 < angle < 3 * (math.pi / 2):
                initial_pos_x = math.floor(player.rect.centerx / settings.TILE_SIZE) * settings.TILE_SIZE
                horizontal_end_pos_x = initial_pos_x - (settings.TILE_SIZE * i)
                horizontal_end_pos_y = player.rect.centery - (
                    tangent * abs(horizontal_end_pos_x - player.rect.centerx)
                )
                # clamp map indexs to map size
                map_index_x = min(
                    int(max(horizontal_end_pos_x / settings.TILE_SIZE, 0)),
                    len(self.map[0]) - 1
                ) -1
                map_index_y = min(
                    int(max(horizontal_end_pos_y / settings.TILE_SIZE, 0)),
                    len(self.map) - 1
                )
            # looking strait to the sides
            else:
                # up
                if angle == 3 * (math.pi/2):
                    horizontal_end_pos_y = 0
                    horizontal_end_pos_x = player.rect.centerx
                # down
                elif angle == math.pi / 2:
                    horizontal_end_pos_y = settings.HEIGHT
                    horizontal_end_pos_x = player.rect.centerx
                else:
                    print('unhandle angle')
                # clamp map indexs to map size
                map_index_y = min(
                    int(max(horizontal_end_pos_y / settings.TILE_SIZE, 0)),
                    len(self.map) - 1
                )
                map_index_x = min(
                    int(max(horizontal_end_pos_x / settings.TILE_SIZE, 0)),
                    len(self.map[0]) - 1
                )

            # get the squared ray lengh (pytagore)
            horizontal_lengh = (
                (abs(player.rect.x - horizontal_end_pos_x) ** 2) +
                (abs(player.rect.y - horizontal_end_pos_y) ** 2)
            )

            # find collision with walls
            if self.map[map_index_y][map_index_x]:
                break

        # check shortest ray
        if vertical_lengh <= horizontal_lengh:
            return vertical_end_pos_x, vertical_end_pos_y, settings.RAY_COLOR_VERTICAL
        return horizontal_end_pos_x, horizontal_end_pos_y, settings.RAY_COLOR_HORIZONTAL

    def normalize_angle(self, angle: float) -> float:
        """ normalize angle ( in radian ) in 0, 2pi
        return a angle in radian """
        while angle < 0:
            angle += 2 * math.pi
        while angle > (2 * math.pi):
            angle -= 2 * math.pi
        return angle

    # i know the D is capital
    # pylint: disable=invalid-name
    def render_2D(self, canvas: pygame.Surface) -> None:
        """ 2D, blit tiles to a canvas render player"""
        canvas.fill(settings.BACKGROUND_COLOR)

        # blit tiles
        for tile in self.tiles:
            tile.render(canvas=canvas)

        # all rays
        for ray_index in range(settings.FOV):
            angle = self.player.angle + math.radians(ray_index - (settings.FOV / 2))
            x, y, color = self.cast_ray(
                player=self.player,
                angle=angle
            )
            pygame.draw.line(
                surface=canvas,
                color=color,
                start_pos=self.player.rect.center,
                end_pos=(x, y),
            )

        self.player.render(canvas=canvas)

        # direction ray
        x, y, color = self.cast_ray(
            player=self.player,
            angle=self.player.angle
        )
        pygame.draw.line(
                surface=canvas,
                color=settings.RAY_DIRECTION_COLOR,
                start_pos=(self.player.rect.centerx + settings.WIDTH, self.player.rect.centery),
                end_pos=(x + settings.WIDTH, y),
            )

    # pylint: disable=invalid-name
    def render_3D(self, canvas: pygame.Surface) -> None:
        """ 3D, draw vertical line for each rays"""
        for ray_index in range((settings.FOV*settings.RESOLUTION_MULTIPLIER) + 1):
            # get angles
            player_angle_normalized = self.normalize_angle(self.player.angle)
            ray_angle = self.normalize_angle(
                player_angle_normalized +
                math.radians((ray_index/settings.RESOLUTION_MULTIPLIER) - (settings.FOV/2))
            )

            # get ray
            ray_x, ray_y, ray_color = self.cast_ray(
                player=self.player,
                angle=ray_angle
            )

            ray_len = math.sqrt(
                (self.player.rect.x - ray_x) ** 2 +
                (self.player.rect.y - ray_y) ** 2
            )

            angle_diff = self.normalize_angle(ray_angle - player_angle_normalized)


            # fix fisheye effect
            ray_len *= math.cos(angle_diff)
            line_height = (settings.HEIGHT * settings.TILE_SIZE) / ray_len

            # center the lines
            start_y = (settings.HEIGHT - line_height) / 2
            end_y = start_y + line_height

            x = (ray_index/settings.RESOLUTION_MULTIPLIER) * (settings.WIDTH / settings.FOV)

            pygame.draw.line(
                surface=canvas,
                color=ray_color,
                start_pos=(x, start_y),
                end_pos=(x, end_y), 
                width=math.ceil(settings.WIDTH / (settings.FOV*settings.RESOLUTION_MULTIPLIER)),
            )


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
