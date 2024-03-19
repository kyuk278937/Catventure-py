import pygame
import Scene
import player
import Block

class TestScene(Scene.Scene):
    def __init__(self):
        super().__init__()

        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 60

        self.screen = self.createWindow(WIDTH=self.WIDTH,
                          HEIGHT=self.HEIGHT,
                          FPS=self.FPS)
        self.debug = True

        self.preload()
        self.update()

    def preload(self):
        self.create_island(0,528,'grass',0,10,self.screen[0])
        self.groundGroup.add(Block.Block(100,528-64,'grass',0,self.screen[0]))

        self.player = player.Player((0, 0),self.groundGroup,self.screen[0])

    def update(self):
        while True:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                return 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0

            self.screen[0].fill((50, 50, 50))


            self.groundGroup.update(self.debug)
            self.player.update(self.debug)

            pygame.display.flip()
            self.screen[1].tick(self.screen[2])