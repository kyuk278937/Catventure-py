import pygame
import Scene
import player
import GameObject
import Block
import Window
import Portal
import SpriteSheet
import SceneManager
import NPC

class ShopScene(Scene.Scene):
    def __init__(self,screen,start_bias_x = 746):
        super().__init__()
        self.start_bias_x = start_bias_x

        self.screen = screen

        self.create_player_info(self.screen[0])
        self.create()
        self.update()

    def create(self):
        self.create_Block_platform(585, 528, 29, 0, 10, self.screen[0])
        self.create_Block_wall(585, 528, 29, 0, 10, self.screen[0])
        self.create_Block_wall(1048+185, 528, 29, 0, 10, self.screen[0])

        board_bg_list = self.create_wall(590,70,pygame.image.load('assets/1659385766_52-kartinkin-net-p-doski-piksel-art-oboi-60.png'),0.55,2,self.screen[0])

        self.groundGroup.add(Block.Block(900,473,0,106,self.screen[0],45))

        self.portalGroup.add(Portal.Portal(1100,443,self.slice_sheet(sheet=pygame.image.load('assets/tilemap_packed.png').convert_alpha(),scale=self.SCALE,spriteSize=self.SPRITE_SIZE)[150],'city',1.3,self.screen[0],1853))

        self.player = player.Player((368, 472), 1, self.groundGroup,self.portalGroup,self.npcGroup, self.screen[0])
        self.player.bias_x = self.start_bias_x

        seller = NPC.NPC(830,483,(830,483,230,64),[pygame.image.load('assets/nps_shop_Idle.png')],self.npcGroup,4,self.screen[0],5)

        for object in board_bg_list:
            self.GameObjectsList[0].append(object)
        self.GameObjectsList[0].append(self.groundGroup)
        self.GameObjectsList[0].append(self.portalGroup)
        self.GameObjectsList[0].append(seller)

    def update(self):
        scen_manager = SceneManager.SceneManager()
        while True:
            self.basick_update(self.player,self.screen,scen_manager,self.debug)