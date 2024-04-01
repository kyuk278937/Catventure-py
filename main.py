import asyncio
import pygame
import TestScene
import Window
import HomeScene
import CityScene
import ShopScene

WIDTH = 800
HEIGHT = 600
FPS = 60

def main():
    window = Window.Window()
    screen = window.createWindow(WIDTH,HEIGHT,FPS)
    #HomeScene.HomeScene(screen)
    #CityScene.CityScene(screen)
    ShopScene.ShopScene(screen)

if __name__ == '__main__':
    main()

# http://localhost:8000#debug