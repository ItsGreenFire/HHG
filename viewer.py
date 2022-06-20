import pygame
from screeninfo import get_monitors

for monitor in get_monitors():
    pass

clock = pygame.time.Clock()


class ViewerClass:
    def __init__(self, width, height, levelimg):
        self.width = width
        self.height = height

        self.levelimg = pygame.transform.scale(pygame.image.load("assets/" + levelimg), (width * .5, height * .5))
        # self.borderimg = pygame.transform.scale(pygame.image.load("assets/border.png"),(width, height))

        self.screen = pygame.display.set_mode([width, height])
        self.levelrect = self.levelimg.get_rect()

        self.sprites = []

    def add_sprite(self, spr):
        self.sprites.append(spr)

    def remove_sprite(self, spr):
        self.sprites.remove(spr)

    def repaint(self):
        self.screen.fill("black")
        self.screen.blit(self.levelimg, self.levelimg.get_rect().center)

        # Print to screen
        for s in self.sprites:
            s.drawSprite(self.screen)
        pygame.display.flip()

    def getscreen(self):
        return self.screen
