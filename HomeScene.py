import pygame
import Scene
import player
import GameObject
import Block
import Window
import Portal
import SpriteSheet
import SceneManager

class HomeScene(Scene.Scene,Window.Window, SpriteSheet.SpriteSheet):
    def __init__(self,screen,start_bias_x = 368):
        super().__init__()
        self.start_bias_x = start_bias_x

        self.screen = screen

        self.create()
        self.update()

    def create(self):
        self.create_Block_platform(585, 528, 29, 0, 10, self.screen[0])
        self.create_Block_wall(585, 528, 29, 0, 10, self.screen[0])
        self.create_Block_wall(1048+185, 528, 29, 0, 10, self.screen[0])

        board_bg_list = self.create_wall(590,70,pygame.image.load('assets/1659385766_52-kartinkin-net-p-doski-piksel-art-oboi-60.png'),0.55,2,self.screen[0])
        bed = GameObject.GameObject(670,470,pygame.image.load('assets/cat_bed.png'),5,self.screen[0])
        bowl = GameObject.GameObject(790,425,pygame.image.load('assets/pet-food-bowl-in-pixel-style_475147-1835-removebg-preview.png'),0.35,self.screen[0])

        self.portalGroup.add(Portal.Portal(1100,443,self.slice_sheet(sheet=pygame.image.load('assets/tilemap_packed.png').convert_alpha(),scale=self.SCALE,spriteSize=self.SPRITE_SIZE)[150],'city',1.3,self.screen[0]))

        self.player = player.Player((368, 472), 1, self.groundGroup,self.portalGroup, self.screen[0])
        self.player.bias_x = self.start_bias_x


        for object in board_bg_list:
            self.GameObjectsList[0].append(object)
        self.GameObjectsList[0].append(self.groundGroup)
        self.GameObjectsList[0].append(bed)
        self.GameObjectsList[0].append(bowl)
        self.GameObjectsList[0].append(self.portalGroup)

    def update(self):
        scen_manager = SceneManager.SceneManager()
        while True:
            self.basick_update(self.player,self.screen,scen_manager,self.debug)