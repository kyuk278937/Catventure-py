import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self,x,y,image,scale,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y

        self.rect = pygame.Rect(x, y, image.get_size()[0] * scale, image.get_size()[1] * scale)
        self.image = pygame.transform.scale(image,(image.get_size()[0]*scale,image.get_size()[1]*scale))

    def update(self, bias_x ,debug=False):
        self.rect[0] = self.x - bias_x

        self.screen.blit(self.image, (self.x - bias_x, self.y))

        if debug: pygame.draw.rect(self.screen, (0, 0, 255), self.rect, 2)