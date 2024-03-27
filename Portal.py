import pygame
import GameObject

class Portal(GameObject.GameObject):
    def __init__(self,x,y,image,next_scene,scale,screen):
        super().__init__(x,y,image,scale,screen)

        self.next_scene = next_scene