import pygame
from player import PlayerClass


class ViewerClass:
    def __init__(self, width, height, levelimg):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([width, height])
        self.levelimg = pygame.transform.scale(pygame.image.load("assets/" + levelimg), (width * .5, height * .5))
        self.levelrect = self.levelimg.get_rect()

    def repaint(self):
        self.screen.fill("black")
        self.screen.blit(self.levelimg, self.levelrect.center)
        self.screen.blit()

        # Print to screen
        pygame.display.flip()

    def getScreen(self):
        return self.screen
