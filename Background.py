import pygame
import GameObject

class Background(GameObject.GameObject):
    def __init__(self,image,scale,interpolation_index,player,screen):
        super().__init__(player.rect.x-(image.get_size()[0]*scale)/2, 0, image, scale, screen)

        self.interpolation_index = interpolation_index

    def update(self, bias_x ,debug=False):
        self.rect[0] = self.x - bias_x//self.interpolation_index

        self.screen.blit(self.image, (self.x - bias_x//self.interpolation_index, self.y))

        if debug: pygame.draw.rect(self.screen, (0, 0, 255), self.rect, 2)