import pygame
import Block
import GameObject
import Window
import SpriteSheet
import Label

class Scene(Window.Window, SpriteSheet.SpriteSheet):
    def __init__(self, start_bias_x = 0):
        self.SPRITE_SIZE = 18
        self.SCALE = 4

        self.ISLAND_INDENTATION = 18

        self.debug = False

        self.start_bias_x = start_bias_x

        self.GameObjectsList = [[],[],[]]

        self.groundGroup = pygame.sprite.Group()
        self.portalGroup = pygame.sprite.Group()
        self.npcGroup = pygame.sprite.Group()

        self.basick_spritesheet = self.slice_sheet(sheet=pygame.image.load('assets/tilemap_packed.png').convert_alpha(),scale=self.SCALE,spriteSize=self.SPRITE_SIZE)

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

    def create_player_info(self,screen):
        self.GameObjectsList[2].append(GameObject.GameObject(20, 25, self.basick_spritesheet[151], 1, screen)) #НЕ змінювати прорядок створення
        self.GameObjectsList[2].append(Label.Label(100,45,"---",48,screen))

        for i in range(5):
            self.GameObjectsList[2].append(GameObject.GameObject(400 + 70*i, 25, self.basick_spritesheet[44], 1, screen))

    def show_player_info(self,player):
        HP = player.get_HP()
        coins = player.get_coins()

        self.GameObjectsList[2][1].set_text(str(coins))

    def basick_update(self,player,screen,scen_manager,debug):
        self.system_update1(screen)
        self.show_player_info(player)

        player_data = player.update(debug)
        bias_x = player_data[0]
        next_scene = player_data[1]

        if next_scene != '':
            scen_manager.run_scene(next_scene, screen, bias_x)
            return

        for object in self.GameObjectsList[0]:
            object.update(bias_x, debug)

        player.draw(debug)

        for object in self.GameObjectsList[1]:
            object.update(bias_x, debug)

        for object in self.GameObjectsList[2]:
            object.update(0,False)

        self.system_update2(screen)