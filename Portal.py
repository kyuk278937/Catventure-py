import pygame
import GameObject

class Portal(GameObject.GameObject):
    def __init__(self,x,y,image,next_scene,scale,screen,bias_x=0):
        super().__init__(x,y,image,scale,screen)

        self.next_scene = next_scene
        self.bias_x = bias_x