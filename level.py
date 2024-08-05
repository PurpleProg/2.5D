""" level class """
import math
import pygame
from player import Player
import settings


class Level:
    """ handle map and raycasting """
    # pylint: disable=C0301
    def __init__(self) -> None:
        self.map_0: list[list[int]] = [
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
        self.map_1: list[list[int]] = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        ]
        self.map_2: list[list[int]] = [
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
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        self.map = self.map_3

        self.player = Player()
        self.tiles = []

        # create tiles
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

    def cast_ray(self, player, angle) -> tuple[int, int]:
        """ draw a line to next wall, use player.angle """

        # normalize angle
        if angle < 0:
            angle += 2 * math.pi
        else:
            while angle > 2 * math.pi:
                angle -= 2 * math.pi

        # calc tangent
        try:
            invert_tangent = 1/math.tan(angle)
        except ZeroDivisionError:
            invert_tangent = 0

        # get nearest line
        initial_pos_y = round(player.rect.centery / settings.TILE_SIZE) * settings.TILE_SIZE
        initial_pos_x = round(player.rect.centerx / settings.TILE_SIZE) * settings.TILE_SIZE

        # vertical rays
        for i in range(1, settings.MAX_RAY_DISTANCE):
            # looking down
            if 0 < angle < math.pi:
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
        for i in range(1, settings.MAX_RAY_DISTANCE):
            # looking right
            if 3 * (math.pi / 2) < angle or angle < math.pi / 2:
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
            return vertical_end_pos_x, vertical_end_pos_y
        return horizontal_end_pos_x, horizontal_end_pos_y

    def render(self, canvas: pygame.Surface) -> None:
        """ blit tiles to a canvas render player"""
        # blit tiles
        for tile in self.tiles:
            tile.render(canvas=canvas)

        # all rays
        for ray_index in range(settings.FOV):
            angle = self.player.angle + math.radians(ray_index - (settings.FOV / 2))
            x, y = self.cast_ray(
                player=self.player,
                angle=angle
            )
            pygame.draw.line(
                surface=canvas,
                color=settings.RAY_COLOR,
                start_pos=self.player.rect.center,
                end_pos=(x, y),
            )

        self.player.render(canvas=canvas)

        # direction ray
        pygame.draw.line(
                surface=canvas,
                color=settings.RAY_DIRECTION_COLOR,
                start_pos=self.player.rect.center,
                end_pos=(self.cast_ray(
                    player=self.player,
                    angle=self.player.angle
                )),
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
