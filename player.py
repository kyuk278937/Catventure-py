import pygame
import SpriteSheet as sp

class Player(pygame.sprite.Sprite,sp.SpriteSheet):
    def __init__(self,pos,groundGroup,screen):
        pygame.sprite.Sprite.__init__(self)
        self. screen = screen

        self.groundGroup = groundGroup

        self.spriteSize = 16
        self.scale = 4
        self.speed = 5
        self.gravity = 0.5
        self.fleep = False
        self.dfleep = False
        self.vel_y = 0

        self.playerIdle = self.slice_sheet(sheet=pygame.image.load('assets/Meow-Knight_Idle.png').convert_alpha(),scale=self.scale,spriteSize=self.spriteSize)

        self.image = self.playerIdle[0]
        self.rect = pygame.Rect(pos[0], pos[1], self.spriteSize * self.scale, self.spriteSize * self.scale)

    def fleep_update(self):
        if self.dfleep != self.fleep:
            self.fleep = self.dfleep
            self.image = pygame.transform.flip(self.image, True, False)
            self.image.set_colorkey((0, 0, 0))

    def draw(self):
        self.fleep_update()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def gravity_(self,isJumping):
        dy = 0

        self.vel_y += self.gravity

        if self.rect.bottom + dy > 600:
            self.vel_y = 0
            dy = 600 - self.rect.bottom

        if isJumping==False:
            for block in self.groundGroup:
                if self.rect.colliderect(block.rect):
                    self.vel_y = 0

        dy += self.vel_y

        return dy

    def move(self):
        dx = 0
        dy = 0

        isJumpitn = False

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -self.speed
            self.dfleep = True
        if key[pygame.K_d]:
            dx = self.speed
            self.dfleep = False
        if key[pygame.K_SPACE]:
            isJumpitn = True
            self.vel_y = -self.speed*2

        self.rect.x += dx
        self.rect.y += self.gravity_(isJumpitn)

    def update(self,debug=False):
        self.draw()
        self.move()

        if debug: pygame.draw.rect(self.screen, (255, 255, 255), self.rect, 2)