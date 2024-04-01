import pygame
pygame.font.init()

class Label():
    def __init__(self,x,y,text,size,screen,color=(255,255,255)):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color
        self.font = pygame.font.Font("assets/CyrBit.ttf",size)

        self.label = self.font.render(text,1,self.color)

    def set_text(self,text):
        self.label = self.font.render(text, 1, self.color)

    def update(self, bias_x ,debug=False):
        self.screen.blit(self.label,(self.x - bias_x, self.y))