import pygame

class Coliders():
    def bottom_colide_group(self,rect,group):
        for block in group:
            if rect.colliderect(block.rect):
                if rect[1] + rect[3] > block.rect[1] and rect[1] < block.rect[1] + block.rect[2]/2 and rect[0] + rect[2] > block.rect[0] + block.rect[2]*0.05 and rect[0] < block.rect[0] + block.rect[2]*0.95:
                    return True
        return False

    def colide_portal(self,rect,portalGroup):
        for portal in portalGroup:
            if rect.colliderect(portal.rect):
                return portal.next_scene, portal.bias_x
        return '',0

    def colide_npc_triger(self,rect,npcGroup):
        for npc in npcGroup:
            if rect.colliderect(npc.rect):
                return True
        return False

    def colide_rect_group(self, rect, vel_x, vel_y, dx, dy, gravity, group):
        dy = dy
        dx = dx
        vel_x = vel_x
        vel_y = vel_y

        for block in group:
            if rect.colliderect(block.rect):
                if rect[1] < block.rect[1] + block.rect[3]*0.75  and rect[1] > block.rect[1] - block.rect[3]*0.75:
                    if rect[0] + rect[2] + vel_x > block.rect[0] and rect[0] + rect[2] + vel_x < block.rect[0] + block.rect[2]/2:
                        vel_x = 0
                        dx = block.rect[0]-rect[2]-rect[0] + 1
                        break
                    if rect[0] + vel_x < block.rect[0] + block.rect[2] and rect[0] + vel_x > block.rect[0] + block.rect[2]/2:
                        vel_x = 0
                        dx = (block.rect[2]+block.rect[0]) - rect[0] - 1
                        break

                if rect[0] + rect[2] > block.rect[0] + block.rect[2]*0.05 and rect[0] < block.rect[0] + block.rect[2]*0.95:
                    if rect[1] + vel_y + rect[3] > block.rect[1] and rect[1] + vel_y < block.rect[1] + block.rect[2]/2:
                        vel_y = 0
                        dy = block.rect[1]-rect[2] - rect[1] + gravity

                    if rect.y + vel_y < block.rect.y + block.rect[2] and rect.y + vel_y > block.rect.y + block.rect[2]/2:
                        dy = block.rect.y + block.rect[2] - rect.y + vel_y
                        vel_y = 0

        return vel_x, vel_y, dx, dy