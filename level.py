""" level class """
import math
import pygame
from player import Player
import settings


class Level:
    """ handle map and ray casting """
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
            [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
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

        # background
        self.floor = pygame.Surface(size=(settings.WIDTH, settings.HEIGHT//2))
        self.floor.fill(color=settings.FLOOR_COLOR)
        self.sky = pygame.Surface(size=(settings.WIDTH, settings.HEIGHT//2))
        self.sky.fill(settings.SKY_COLOR)

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

    def cast_vertical_ray(self, player, angle) -> tuple[int, int, int]:
        """ calc line to the nearest vertical wall """

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
                # clamp map indexes to map size
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
                # clamp map indexes to map size
                map_index_y = min(
                    int(max(vertical_end_pos_y / settings.TILE_SIZE, 0)),
                    len(self.map) - 1
                ) - 1
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
                    raise ValueError(f'unhandled angle : {angle}')
                # clamp map indexes to map size
                map_index_y = min(
                    int(max(vertical_end_pos_y / settings.TILE_SIZE, 0)),
                    len(self.map) - 1
                )
                map_index_x = min(
                    int(max(vertical_end_pos_x / settings.TILE_SIZE, 0)),
                    len(self.map[0]) - 1
                )

            # get the ray squared length (pytagore)
            vertical_length_squared = (
                ((player.rect.x - vertical_end_pos_x) ** 2) +
                ((player.rect.y - vertical_end_pos_y) ** 2)
            )

            # find collision with walls
            if self.map[map_index_y][map_index_x]:
                break

        return vertical_end_pos_x, vertical_end_pos_y, vertical_length_squared

    def cast_horizontal_ray(self, player, angle) -> tuple[int, int, int]:
        """ calc a line to the nearest horizontal wall """

        angle = self.normalize_angle(angle=angle)

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
                # clamp map indexes to map size
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
                # clamp map indexes to map size
                map_index_x = min(
                    int(max(horizontal_end_pos_x / settings.TILE_SIZE, 0)),
                    len(self.map[0]) - 1
                ) - 1
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
                    print('unhandled angle')
                # clamp map indexes to map size
                map_index_y = min(
                    int(max(horizontal_end_pos_y / settings.TILE_SIZE, 0)),
                    len(self.map) - 1
                )
                map_index_x = min(
                    int(max(horizontal_end_pos_x / settings.TILE_SIZE, 0)),
                    len(self.map[0]) - 1
                )

            # get the squared ray length (pytagore)
            horizontal_length = (
                (abs(player.rect.x - horizontal_end_pos_x) ** 2) +
                (abs(player.rect.y - horizontal_end_pos_y) ** 2)
            )

            # find collision with walls
            if self.map[map_index_y][map_index_x]:
                break

        return horizontal_end_pos_x, horizontal_end_pos_y, horizontal_length

    def cast_ray(self, player: Player, angle: float) -> tuple[int, int, int, str]:
        """ returns: x, y, len, color """
        # get vertical ray
        vertical_ray_x, vertical_ray_y, vertical_ray_len_squared = self.cast_vertical_ray(
            player=self.player,
            angle=angle
        )

        # get horizontal ray
        horizontal_ray_x, horizontal_ray_y, horizontal_ray_len_squared = self.cast_horizontal_ray(
            player=self.player,
            angle=angle,
        )

        angle_diff = self.normalize_angle(angle - self.normalize_angle(self.player.angle))

        # get the shortest ray by squared len
        if vertical_ray_len_squared <= horizontal_ray_len_squared:
            ray_x = vertical_ray_x
            ray_y = vertical_ray_y
            ray_len_squared = vertical_ray_len_squared
            # print(f' angle:{ray_angle}, cos:{math.cos(ray_angle)}')
            # ray_len = (
            #     (self.player.rect.y - ray_y) / math.cos(self.normalize_angle(ray_angle - (math.pi/2)))
            # )
            ray_len = math.sqrt(ray_len_squared)
            ray_color = settings.RAY_COLOR_VERTICAL
        else:
            ray_x = horizontal_ray_x
            ray_y = horizontal_ray_y
            ray_len_squared = horizontal_ray_len_squared
            # ray_len = (
            #     (self.player.rect.x - ray_x) / math.cos(ray_angle)
            # )
            ray_len = math.sqrt(ray_len_squared)
            ray_color = settings.RAY_COLOR_HORIZONTAL

        # fix fisheye effect
        ray_len *= math.cos(angle_diff)

        return ray_x, ray_y, ray_len, ray_color

    def normalize_angle(self, angle: float) -> float:
        """ normalize angle ( in radian ) in 0, 2pi
        return a angle in radian """
        while angle < 0:
            angle += 2 * math.pi
        while angle > (2 * math.pi):
            angle -= 2 * math.pi
        return angle

    # I know the D is capital
    # pylint: disable=invalid-name
    def render_2D(self, canvas: pygame.Surface) -> None:
        """ 2D, blit tiles to a canvas render player"""
        canvas.fill(settings.BACKGROUND_COLOR)

        # blit tiles
        for tile in self.tiles:
            tile.render(canvas=canvas)

        # all rays
        for ray_index in range(int(settings.FOV * settings.RESOLUTION_MULTIPLIER)):

            # get x position
            # x = (ray_index / settings.RESOLUTION_MULTIPLIER) * (settings.WIDTH / settings.FOV)

            # relative_angle = math.atan(
                    # (x - (settings.WIDTH / 2)) / settings.PROJECTION_DISTANCE
                # )

            # ray_angle = self.player.angle + relative_angle * (settings.FOV / 70)

            ray_angle = self.player.angle + math.radians((ray_index / settings.RESOLUTION_MULTIPLIER) - (settings.FOV / 2))

            ray_x, ray_y, ray_len, ray_color = self.cast_ray(player=self.player, angle=ray_angle)

            pygame.draw.line(
                surface=canvas,
                color=ray_color,
                start_pos=self.player.rect.center,
                end_pos=(ray_x, ray_y),
            )

        self.player.render(canvas=canvas)

    # pylint: disable=invalid-name
    def render_3D(self, canvas: pygame.Surface) -> None:
        """ 3D, draw vertical line for each rays"""

        # draw floor and sky
        canvas.blit(
            source=self.floor,
            dest=(0, settings.HEIGHT//2)
        )
        canvas.blit(
            source=self.sky,
            dest=(0, 0)
        )

        # draw walls
        for ray_index in range(int(settings.FOV*settings.RESOLUTION_MULTIPLIER) + 1):

            # get x position
            x = (ray_index/settings.RESOLUTION_MULTIPLIER) * (settings.WIDTH / settings.FOV)

            ray_angle = self.player.angle + math.atan(
                    (x - (settings.WIDTH / 2)) / settings.PROJECTION_DISTANCE
                )

            ray_x, ray_y, ray_len, ray_color = self.cast_ray(player=self.player, angle=ray_angle)

            line_height = min(
                ((settings.HEIGHT * settings.TILE_SIZE) / ray_len),
                settings.HEIGHT,
            )

            # center the lines
            start_y = (settings.HEIGHT - line_height) / 2
            end_y = start_y + line_height

            # draw a vertical line for each ray
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
