import pygame

import Portal
import Scene
import player
import Block
import Window
import SceneManager
import GameObject
import SpriteSheet
import Background

class CityScene(Scene.Scene):
    def __init__(self, screen, start_bias_x = 0):
        super().__init__()
        self.start_bias_x = start_bias_x

        self.screen = screen

        self.create_player_info(self.screen[0])
        self.create()
        self.update()

    def create(self):
        self.create_Block_island(-400,528,'grass',0,100,self.screen[0])

        self.player = player.Player((368, 472),1,self.groundGroup,self.portalGroup,self.npcGroup,self.screen[0])
        self.player.bias_x = self.start_bias_x

        home = GameObject.GameObject(575,163,pygame.image.load('assets/1146000c972c87c1d9d359fe8fb73ce2839a826f.png'),6,self.screen[0])
        lamp1 = GameObject.GameObject(950, 230, pygame.image.load('assets/QXuedJ.png'),2.5, self.screen[0])
        lamp2 = GameObject.GameObject(1940, 230, pygame.image.load('assets/QXuedJ.png'), 2.5, self.screen[0])
        grass = GameObject.GameObject(1030, 509,pygame.image.load('assets/grass1.png'),4, self.screen[0])
        house1 = GameObject.GameObject(1130, 168, pygame.image.load('assets/8c76c6294ff330448b56591485753d9044c041ea.png'),6, self.screen[0])
        house2 = GameObject.GameObject(1500, 161,pygame.image.load('assets/135-1352896_cabin-clipart-pixel-art-pixel-art-log-cabin-removebg-preview.png'), 0.9,self.screen[0])
        shop = GameObject.GameObject(2100, 0, pygame.image.load('assets/b0e1yo5etyv61.png'), 0.5, self.screen[0])
        bench = GameObject.GameObject(100,440,pygame.image.load('assets/bench.png'),0.3,self.screen[0])
        tree = GameObject.GameObject(-150,153,pygame.image.load('assets/tree.png'),8,self.screen[0])

        self.portalGroup.add(Portal.Portal(727,450,pygame.image.load('assets/nothing.png'),'home',5,self.screen[0],746))
        self.portalGroup.add(Portal.Portal(2207, 450, pygame.image.load('assets/nothing.png'), 'shop', 6, self.screen[0], 746))

        background = Background.Background(pygame.image.load('assets/background.png'),8,3,self.player,self.screen[0])

        invisible_wall = self.create_wall(-85,528,pygame.image.load('assets/nothing.png'),4,10,self.screen[0])
        for i in range(len(invisible_wall)):
            self.groundGroup.add(invisible_wall[i])

        invisible_wall = self.create_wall(2900, 472, self.slice_sheet(sheet=pygame.image.load('assets/tilemap_packed.png').convert_alpha(),scale=self.SCALE,spriteSize=self.SPRITE_SIZE)[6], 1, 10, self.screen[0])
        for i in range(len(invisible_wall)):
            self.groundGroup.add(invisible_wall[i])

        self.GameObjectsList[0].append(background)
        self.GameObjectsList[0].append(self.groundGroup)
        self.GameObjectsList[0].append(home)
        self.GameObjectsList[0].append(lamp1)
        self.GameObjectsList[0].append(lamp2)
        self.GameObjectsList[0].append(grass)
        self.GameObjectsList[0].append(house1)
        self.GameObjectsList[0].append(house2)
        self.GameObjectsList[0].append(shop)
        self.GameObjectsList[0].append(tree)
        self.GameObjectsList[0].append(bench)
        self.GameObjectsList[0].append(self.portalGroup)

    def update(self):
        scen_manager = SceneManager.SceneManager()
        while True:
            self.basick_update(self.player, self.screen, scen_manager, self.debug)