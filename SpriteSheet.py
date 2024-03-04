import pygame

class SpriteSheet():
    def slice_sheet(self,sheet,scale,spriteSize):
        sheetLenX = sheet.get_size()[0]
        sheetLenY = sheet.get_size()[1]
        spryts = list()
        for i in range(sheetLenY//spriteSize):
            for j in range(sheetLenX//spriteSize):
                image = pygame.Surface((spriteSize,spriteSize)).convert_alpha()
                image.blit(sheet,(0,0),(j*spriteSize,i*spriteSize,j*spriteSize+spriteSize,i*spriteSize+spriteSize))
                image = pygame.transform.scale(image,(spriteSize*scale,spriteSize*scale))
                image.set_colorkey((0, 0, 0))
                spryts.append(image)
        return spryts