""" copyleft
Licence: GPL-3+
"""
import sys
import pygame
from level import Level


class Game:
    """ main game, hold global var """
    def __init__(self) -> None:
        pygame.init()

        # init display
        self.display: pygame.Surface = pygame.display.set_mode(size=(1024, 512))
        # self.display = pygame.display.set_mode(size=(1024, 512), flags=pygame.FULLSCREEN)
        pygame.display.set_caption('2.5D engine')

        # clock for FPS
        self.clock = pygame.Clock()
        self.FPS = 60

        self.level = Level()

        self.running = True

    def mainloop(self) -> None:
        """ executed each frame """
        while self.running:
            self.handel_events()
            self.update()
            self.render()

    def handel_events(self) -> None:
        """ get events """
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    sys.exit()

    def update(self) -> None:
        """ update the level """
        # self.level.update()

    def render(self) -> None:
        """ render the level """

        self.level.render(self.display)

        pygame.display.flip()
        self.clock.tick(self.FPS)


def main() -> None:
    """ main entrypoint """
    game = Game()
    game.mainloop()


if __name__ == '__main__':
    main()
