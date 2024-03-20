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
        self.debug = False

        self.preload()
        self.update()

    def preload(self):
        self.create_island(0,528,'grass',0,10,self.screen[0])
        self.groundGroup.add(Block.Block(100,528 - 45,'grass',0,self.screen[0]))
        self.groundGroup.add(Block.Block(100, 528 - 200, 'grass', 0, self.screen[0]))

        self.player = player.Player((400-32, 0),1,self.groundGroup,self.screen[0])

    def update(self):
        while True:
            self.system_update1(self.screen)

            bias_x = self.player.update(self.debug)

            self.groundGroup.update(bias_x, self.debug)

            self.player.draw(self.debug)

            self.system_update2(self.screen)