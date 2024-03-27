import pygame
import Block
import GameObject
import Window

class Scene(Window.Window):
    def __init__(self, start_bias_x = 0):
        self.SPRITE_SIZE = 18
        self.SCALE = 4

        self.ISLAND_INDENTATION = 18

        self.debug = False

        self.start_bias_x = start_bias_x

        self.GameObjectsList = [[],[]]

        self.groundGroup = pygame.sprite.Group()
        self.portalGroup = pygame.sprite.Group()

        self.grassType = {
            'grass': 0,
            'sand': 40,
            'snow': 60
        }

    def create_Block_island(self,x,y,type,layer,len,screen): #Створюе острів з блоків, що має початковий і кінцевий блок
        self.groundGroup.add(Block.Block(x,y,layer,self.grassType[type]+1,screen,self.ISLAND_INDENTATION))
        for i in range(1,len+1):
            self.groundGroup.add(Block.Block(x+ self.SPRITE_SIZE*self.SCALE*i, y, layer, self.grassType[type] + 2,screen,self.ISLAND_INDENTATION))
        self.groundGroup.add(Block.Block(x + self.SPRITE_SIZE*self.SCALE*(len+1), y, layer, self.grassType[type] + 3,screen,self.ISLAND_INDENTATION))

    def create_Block_platform(self,x,y,spryte,layer,len,screen): #Створює платформу з блоків, що мають однакове зображення
        for i in range(0,len):
            self.groundGroup.add(Block.Block(x+ self.SPRITE_SIZE*self.SCALE*i, y, layer, spryte, screen,self.ISLAND_INDENTATION))

    def create_Block_wall(self,x,y,spryte,layer,len,screen): #Створює стіну з блоків, що мають однакове зображення
        for i in range(0,len):
            self.groundGroup.add(Block.Block(x, y - self.SPRITE_SIZE*self.SCALE*i, layer, spryte, screen,0))

    def create_wall(self,x,y,image,scale,len,screen): # Створює стіну з ігрових об'єктір й повертає їх
        objects = list()
        for i in range(0,len):
            objects.append(GameObject.GameObject(x, y - image.get_size()[1]*scale*i, image, scale, screen))
        return objects

    def basick_update(self,player,screen,scen_manager,debug):
        self.system_update1(screen)

        player_data = player.update(debug)
        bias_x = player_data[0]
        next_scene = player_data[1]

        for object in self.GameObjectsList[0]:
            object.update(bias_x, debug)

        player.draw(debug)

        for object in self.GameObjectsList[1]:
            object.update(bias_x, debug)

        self.system_update2(screen)

        if next_scene != '':
            scen_manager.run_scene(next_scene, screen)
            return