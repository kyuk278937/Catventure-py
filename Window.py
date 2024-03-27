import pygame

class Window():
    def createWindow(self,WIDTH, HEIGHT, FPS):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
        #screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.FULLSCREEN, vsync=1)
        pygame.display.set_caption("Catventure")
        pygame.display.set_icon(pygame.image.load('assets/icon.png'))

        clock = pygame.time.Clock()

        return [screen, clock, FPS]

    def system_update1(self,screen):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            return 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

        screen[0].fill((20, 20, 20))

    def system_update2(self, screen):
        pygame.display.flip()
        screen[1].tick(screen[2])