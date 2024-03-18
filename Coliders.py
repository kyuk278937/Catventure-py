import pygame

class Coliders():
    def colide_rect_group(self, rect, vel_x, vel_y, dx, dy, gravity, group):
        dy = dy
        dx = dx
        vel_x = vel_x
        vel_y = vel_y

        for block in group:
            if rect.colliderect(block.rect):
                #print(rect)
                
                if rect[0] + rect[2] + vel_x > block.rect[0] and rect[0] + rect[2] + block.rect[2] < block.rect[0] + block.rect[2]/2:
                    vel_x = 0
                    dx = block.rect[0]-rect[2]-rect[0]
                    print(1)
                    break

                if rect[1] + vel_y + rect[3] > block.rect[1] and rect[1] + vel_y < block.rect[1] + block.rect[2]/2:
                    vel_y = 0
                    dy = block.rect[1]-rect[2] - rect[1] + gravity
            
                if rect.y + vel_y < block.rect.y + block.rect[2] and rect.y + vel_y > block.rect.y + block.rect[2]/2:
                    dy = block.rect.y + block.rect[2] - rect.y + vel_y
                    vel_y = 0

        return vel_x, vel_y, dx, dy