import pygame
from screeninfo import get_monitors

for monitor in get_monitors():
    pass

clock = pygame.time.Clock()
pygame.init()


class ViewerClass:
    def __init__(self, width, height, platename):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([width, height])

        # self.borderimg = pygame.transform.scale(pygame.image.load("assets/border.png"),(width, height))
        self.plateimg = pygame.image.load(platename)

        self.sprites = []

    def add_sprite(self, spr):
        self.sprites.append(spr)

    def remove_sprite(self, spr):
        self.sprites.remove(spr)

    def repaint(self):
        pygame.display.set_caption("Horrific Horrors", "HH")
        pygame.display.set_icon(pygame.image.load('assets/settingsGear.png'))
        self.screen.fill("black")

        # Print to screen
        for s in self.sprites:
            s.drawSprite(self.screen)

        self.screen.blit(self.plateimg, (100 + 1 * 32, 100 + 1 * 32))

        pygame.display.flip()
