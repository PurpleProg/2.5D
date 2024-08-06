""" copyleft
Licence: GPL-3+
"""
import sys
import pygame
from level import Level
import settings


class Game:
    """ main game, hold global var """
    def __init__(self) -> None:
        pygame.init()

        # init display
        self.display: pygame.Surface = pygame.display.set_mode(
            size=(settings.WIDTH+700, settings.HEIGHT)
        )
        pygame.display.set_caption('2.5D engine')

        # clock for fps
        self.clock = pygame.Clock()

        self.level = Level()
        self.keys: set[str] = set()
        self.running = True

    def mainloop(self) -> None:
        """ executed each frame """
        while self.running:
            self.handel_events()
            self.update()
            self.render()

    def handel_events(self) -> None:
        """ store event in the game.keys set """
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    sys.exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            self.running = False
                            pygame.quit()
                            sys.exit()
                        case pygame.K_RIGHT:
                            self.keys.add('RIGHT')
                        case pygame.K_LEFT:
                            self.keys.add('LEFT')
                        case pygame.K_UP:
                            self.keys.add('UP')
                        case pygame.K_DOWN:
                            self.keys.add('DOWN')
                        case pygame.K_a:
                            self.keys.add('a')
                        case pygame.K_d:
                            self.keys.add('d')
                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_RIGHT:
                            self.keys.remove('RIGHT')
                        case pygame.K_LEFT:
                            self.keys.remove('LEFT')
                        case pygame.K_UP:
                            self.keys.remove('UP')
                        case pygame.K_DOWN:
                            self.keys.remove('DOWN')
                        case pygame.K_a:
                            self.keys.remove('a')
                        case pygame.K_d:
                            self.keys.remove('d')

    def update(self) -> None:
        """ update the level """
        self.level.update(self.keys)

    def render(self) -> None:
        """ render the level """
        self.display.fill(settings.BACKGROUND_COLOR)

        self.level.render_2D(self.display)
        self.level.render_3D(self.display)

        pygame.display.flip()
        self.clock.tick(settings.FPS)


def main() -> None:
    """ main entrypoint """
    game = Game()
    game.mainloop()


if __name__ == '__main__':
    main()
