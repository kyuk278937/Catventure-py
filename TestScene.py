import pygame
import Scene
import Player
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
        self.groundGroup.add(Block.Block(100,300,'grass',0,self.screen[0]))

        self.player = Player.Player((0, 0),self.groundGroup,self.screen[0])

    def update(self):
        while True:
            self.system_update(screen=self.screen)

            self.groundGroup.update(self.debug)

            self.player.update(self.debug)