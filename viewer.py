import pygame

clock = pygame.time.Clock()


class ViewerClass:
    def __init__(self, width, height, levelimg, frames):
        self.width = width
        self.height = height
        self.frames = frames
        self.index = 0
        self.screen = pygame.display.set_mode([width, height])
        self.levelimg = pygame.transform.scale(pygame.image.load("assets/" + levelimg), (width * .5, height * .5))
        self.levelrect = self.levelimg.get_rect()

    def repaint(self):
        self.screen.fill("white")
        self.screen.blit(self.levelimg, self.levelimg.get_rect().center)
        # Print to screen
        pygame.display.flip()

    def getScreen(self):
        return self.screen
