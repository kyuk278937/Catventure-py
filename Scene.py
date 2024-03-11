import pygame
import Block

class Scene():
    def __init__(self):
        self.SPRITE_SIZE = 18
        self.SCALE = 4

        self.ISLAND_INDENTATION = 18

        self.groundGroup = pygame.sprite.Group()

        self.grassType = {
            'grass': 0,
            'sand': 40,
            'snow': 60
        }

    def createWindow(self,WIDTH, HEIGHT, FPS):
        pygame.init()
        #screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.FULLSCREEN, vsync=1)
        pygame.display.set_caption("Catventure")
        pygame.display.set_icon(pygame.image.load('assets/icon.png'))

        clock = pygame.time.Clock()

        return [screen, clock, FPS]

    def create_island(self,x,y,type,layer,len,screen):
        self.groundGroup.add(Block.Block(x,y,layer,self.grassType[type]+1,screen,self.ISLAND_INDENTATION))
        for i in range(1,len+1):
            self.groundGroup.add(Block.Block(x+ self.SPRITE_SIZE*self.SCALE*i, y, layer, self.grassType[type] + 2,screen,self.ISLAND_INDENTATION))
        self.groundGroup.add(Block.Block(x + self.SPRITE_SIZE*self.SCALE*(len+1), y, layer, self.grassType[type] + 3,screen,self.ISLAND_INDENTATION))

    def system_update(self,screen):
        screen[1].tick(screen[2])
        pygame.display.update()
        screen[0].fill((50, 50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0