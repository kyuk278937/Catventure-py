import pygame
import SpriteSheet as sp

class Block(pygame.sprite.Sprite,sp.SpriteSheet):
    def __init__(self,x,y,layer,sprite,screen,indentation=0):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.SPRITE_SIZE = 18
        self.SCALE = 4
        self.x = x
        self.y = y
        self.layer = layer

        self.rect = pygame.Rect(x, y + indentation, self.SPRITE_SIZE * self.SCALE,
                                self.SPRITE_SIZE * self.SCALE - indentation)
        self.image = self.slice_sheet(sheet=pygame.image.load('assets/tilemap_packed.png').convert_alpha(),scale=self.SCALE,spriteSize=self.SPRITE_SIZE)[sprite]

    def update(self,debug=False):
        self.screen.blit(self.image, (self.x, self.y))

        if debug: pygame.draw.rect(self.screen, (0, 0, 255), self.rect, 2)