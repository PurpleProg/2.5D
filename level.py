""" level class """
import math
import pygame
from player import Player
from utils import Tile


class Level:
    """ handle map and raycasting """
    def __init__(self) -> None:
        self.map_0: list[list[int]] = [
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
        self.map_1: list[list[int]] = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        ]
        self.map_2: list[list[int]] = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        ]


        self.map = self.map_2

        self.player = Player()
        self.tiles = []

        # create tiles
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

    def cast_ray(self, canvas: pygame.Surface, player, color, angle) -> None:
        """ draw a line to next wall, use player.angle """

        # avoid undef tangent
        if abs(math.cos(angle)) < 1e-10:
            return

        # calc tangent once per frame
        try:
            invert_tangent = (1/math.tan(angle))
        except ZeroDivisionError:
            invert_tangent = 0.01

        # get nearest line
        initial_pos_y = round(player.rect.centery / 64) * 64

        # the ray goes max 10 * 64 if no wall are found.
        # this loop should be break in a normal use
        for i in range(1, 11):
            # looking down
            if 0 < angle and angle < math.pi:
                end_pos_y = initial_pos_y + (64 * i)
                end_pos_x = player.rect.centerx + (invert_tangent * abs(end_pos_y - player.rect.centery))
                # clamp map indexs to map size
                map_index_y = min(int(max(end_pos_y / 64, 0)), len(self.map) - 1)
                map_index_x = min(int(max(end_pos_x / 64, 0)), len(self.map[0]) - 1)
            # looking up
            elif math.pi < angle and angle < 2 * math.pi:
                end_pos_y = initial_pos_y - (64 * i)
                end_pos_x = player.rect.centerx - (invert_tangent * abs(end_pos_y - player.rect.centery))
                # clamp map indexs to map size
                map_index_y = min(int(max(end_pos_y / 64, 0)), len(self.map) - 1) -1
                map_index_x = min(int(max(end_pos_x / 64, 0)), len(self.map[0]) - 1)
            # looking strait to the sides
            else:
                # left
                if angle == math.pi:
                    end_pos_y = self.player.rect.centery
                    end_pos_x = 0
                    # print(angle)
                # right
                elif angle == 0:
                    end_pos_y = self.player.rect.centery
                    end_pos_x = 1024    #  must be greater than screen width 1024
                else:
                    print('unhandle angle')
                # clamp map indexs to map size
                map_index_y = min(int(max(end_pos_y / 64, 0)), len(self.map) - 1)
                map_index_x = min(int(max(end_pos_x / 64, 0)), len(self.map[0]) - 1)

            # find collision with walls
            if self.map[map_index_y][map_index_x]:
                break

        pygame.draw.line(
            surface=canvas,
            color=color,
            start_pos=player.rect.center,
            end_pos=(end_pos_x, end_pos_y)
        )

    def _hmmm(self, player) -> None:
        #---Horizontal---
        iteration=0
        disH=100000
        Tan=1.0/Tan
        if (math.sin(degToRad(ray_angle))> 0.001):
            ray_y=((int(player_y/64)) * 64) -0.0001
            ray_x=(player_y-ray_y)*Tan+player_x
            offset_y = -64
            offset_x = -offset_y * Tan
        #looking up
        elif (sin(degToRad(ray_angle))<-0.001):
            ray_y = (int(player_y/64) * 64 ) + 64
            ray_x = (player_y-ray_y) * Tan + player_x
            offset_y = 64
            offset_x = -offset_y*Tan
        #looking down
        else:
            ray_x = player_x
            ray_y = player_y
            dof=8    #looking straight left or right

        while (dof<8):
            map_x= ray_x // 6
            map_y= ray_y // 6
            mp = map_y * mapX + map_x
            if (mp>0 and mp<mapX*map_x and map[mp]==1):
                dof=8
                disH=cos(degToRad(ray_angle))*(ray_x-player_x)-sin(math.radians(ray_angle))*(ray_x-player_x)   # hit
            else:
                ray_x+=offset_x
                ray_y+=offset_y
                dof+=1

    def render(self, canvas: pygame.Surface) -> None:
        """ blit tiles to a canvas render player"""
        # blit tiles
        for tile in self.tiles:
            tile.render(canvas=canvas)

        self.player.render(canvas=canvas)

        for angle in range(90):
            self.cast_ray(
                canvas=canvas,
                player=self.player,
                color='#0000ff',
                angle=math.radians(angle*4)
            )
        # direction ray
        self.cast_ray(
            canvas=canvas,
            player=self.player,
            color='#00ffff',
            angle=self.player.angle
        )
