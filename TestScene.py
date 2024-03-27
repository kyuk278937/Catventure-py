import pygame
import Scene
import player
import Block
import Window
import SpriteSheet
import SceneManager

class TestScene(Scene.Scene,Window.Window, SpriteSheet.SpriteSheet):
    def __init__(self, screen, start_bias_x = 0):
        super().__init__()
        self.start_bias_x = start_bias_x

        self.screen = screen

        self.preload()
        self.update()

    def preload(self):
        self.create_Block_island(0,528,'grass',0,100,self.screen[0])
        #self.groundGroup.add(Block.Block(100,528 - 45,'grass',0,self.screen[0]))
        #self.groundGroup.add(Block.Block(100, 528 - 200, 'grass', 0, self.screen[0]))

        self.player = player.Player((400-32, 0),1,self.groundGroup,self.screen[0])

    def update(self):
        scen_manager = SceneManager.SceneManager()
        while True:
            self.basick_update(self.player, self.screen, scen_manager, self.debug)