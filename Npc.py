import pygame
import SpriteSheet

class NPC(pygame.sprite.Sprite, SpriteSheet.SpriteSheet):
    def __init__(self,x,y,triger_rect,sprite_sheet_list,npc_group,scale,screen,anim_bias=-1):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.fleep = False

        self.idle_sheet = self.slice_sheet(sprite_sheet_list[0],scale,16)

        self.rect = pygame.Rect(triger_rect[0],triger_rect[1],triger_rect[2],triger_rect[3])
        self.image = self.idle_sheet[0]

        self.anim_frame = anim_bias
        self.ANIM_FRAME_SCALE = 6
        self.anim_frame_scale = 6
        self.anim_delay = 0
        self.last_anim = self.idle_sheet

        self.status = 'idle'

        npc_group.add(self)

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
            self.status = next_status
        self.fleep_update()

    def anim_controller(self):
        match self.status:
            case "idle":
                self.play_anim(self.idle_sheet)

    def fleep_update(self):
        if self.fleep:
            self.image = pygame.transform.flip(self.image, True, False)
            self.image.set_colorkey((0, 0, 0))

    def update(self, bias_x ,debug=False):
        self.anim_controller()

        self.rect[0] = self.x - bias_x

        self.screen.blit(self.image, (self.x - bias_x, self.y))

        if debug: pygame.draw.rect(self.screen, (0, 0, 255), self.rect, 2)
