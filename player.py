import pygame
import SpriteSheet as sp
import Coliders

class Player(pygame.sprite.Sprite,sp.SpriteSheet,Coliders.Coliders):
    def __init__(self,pos,layer,groundGroup,portalGroup,npcGroup,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.groundGroup = groundGroup
        self.portalGroup = portalGroup
        self.npcGroup = npcGroup

        self.HP = 5
        self.coins = 0

        self.spriteSize = 16
        self.scale = 4
        self.SPEED = 3
        self.speed = 3
        self.gravity = 0.5
        self.fleep = False
        self.dfleep = False
        self.vel_y = 0
        self.vel_x = 0

        self.playerIdle = self.slice_sheet(sheet=pygame.image.load('assets/Meow-Knight_Idle.png').convert_alpha(),scale=self.scale,spriteSize=self.spriteSize)
        self.playerWalk = self.slice_sheet(sheet=pygame.image.load('assets/Meow-Knight_Run.png').convert_alpha(),scale=self.scale,spriteSize=self.spriteSize)
        self.playerJump = self.slice_sheet(sheet=pygame.image.load('assets/Meow-Knight_Dodge.png').convert_alpha(),scale=self.scale, spriteSize=self.spriteSize)

        self.image = self.playerIdle[0]
        self.rect = pygame.Rect(pos[0], pos[1], self.spriteSize * self.scale, self.spriteSize * self.scale)

        self.bias_x = self.rect.x

        self.anim_frame = -1
        self.ANIM_FRAME_SCALE = 6
        self.anim_frame_scale = 6
        self.anim_delay = 0
        self.last_anim = list()

        self.player_status = "idle"

        self.next_scene = ''
        self.portal_delay = 35
        self.portal_delay_count = 0

    def get_HP(self):
        return self.HP
    def get_coins(self):
        return self.coins

    def play_anim(self,anim_frams_list):
        if self.last_anim != anim_frams_list:
            self.anim_delay = self.anim_frame_scale
            self.anim_frame = -1
            self.last_anim = anim_frams_list

        if self.anim_delay < self.anim_frame_scale:
            self.anim_delay += 1
            return

        self.anim_delay = 0
        self.anim_frame = (self.anim_frame + 1)%len(anim_frams_list)
        self.image = anim_frams_list[self.anim_frame]

        self.fleep_update()

    def play_anim_ones(self,anim_frams_list,next_status):
        if self.last_anim != anim_frams_list:
            self.anim_delay = self.anim_frame_scale
            self.anim_frame = -1
            self.last_anim = anim_frams_list

        if self.anim_delay < self.anim_frame_scale:
            self.anim_delay += 1
            return

        self.anim_delay = 0
        self.anim_frame = self.anim_frame + 1
        if self.anim_frame < len(anim_frams_list):
            self.image = anim_frams_list[self.anim_frame]
        else:
            self.fleep_update()
            self.anim_frame = -1
            self.player_status = next_status
        self.fleep_update()

    def anim_controller(self):
        match self.player_status:
            case "jump":
                self.play_anim_ones(self.playerJump,"idle")
                return
            case "idle":
                self.play_anim(self.playerIdle)
            case "walk":
                self.play_anim(self.playerWalk)


    def fleep_update(self):
        if self.fleep:
            self.image = pygame.transform.flip(self.image, True, False)
            self.image.set_colorkey((0, 0, 0))

    def draw(self,debug=False):
        self.anim_controller()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        if debug: pygame.draw.rect(self.screen, (255, 255, 255), self.rect, 2)

    def collisions(self):
        dy = 0
        dx = 0

        self.vel_y += self.gravity

        if self.rect.bottom + dy > 600:
            self.vel_y = 0
            dy = 600 - self.rect.bottom
        

        self.vel_x, self.vel_y, dx, dy = self.colide_rect_group(rect = self.rect, vel_x = self.vel_x, vel_y = self.vel_y, dx = dx, dy = dy, gravity = self.gravity, group = self.groundGroup)

        dy += self.vel_y
        dx += self.vel_x
        return dx, dy

    def check_portal(self,key):
        next_scene, bias_x = self.colide_portal(self.rect,self.portalGroup)
        if key[pygame.K_e] and self.portal_delay_count >= self.portal_delay and next_scene != '':
            self.next_scene, self.bias_x = next_scene, bias_x
        else:
            self.portal_delay_count += 1

    def move(self,key):
        self.vel_x = 0

        self.player_status = "idle" if self.player_status != "jump" else "jump"

        if key[pygame.K_a]:
            self.vel_x = -self.speed
            self.fleep = True
            self.player_status = "walk" if self.player_status != "jump" else "jump"
        if key[pygame.K_d]:
            self.vel_x = self.speed
            self.player_status = "walk" if self.player_status != "jump" else "jump"
            self.fleep = False

        if key[pygame.K_LSHIFT] and (key[pygame.K_d] or key[pygame.K_a]):
            self.speed = int(self.SPEED * 1.7)
            self.anim_frame_scale = int(self.ANIM_FRAME_SCALE/1.3)
        else:
            self.anim_frame_scale = self.ANIM_FRAME_SCALE
            self.speed = self.SPEED

        if key[pygame.K_SPACE] and self.bottom_colide_group(self.rect,self.groundGroup):
            self.vel_y = -self.SPEED*4
            self.player_status = 'jump'
            self.anim_frame = -1

        d = self.collisions()
        #self.rect.x += d[0]
        self.bias_x += d[0]
        self.rect.y += d[1]

    def update(self,debug=False):
        key = pygame.key.get_pressed()
        self.move(key)
        self.check_portal(key)
        #print(self.colide_npc_triger(self.rect,self.npcGroup))

        #print(self.bias_x , ' ' , self.rect.y)

        return [self.bias_x, self.next_scene]