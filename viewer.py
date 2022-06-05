import pygame

viewerBackground = (0, 0, 0)
blockWidth = 32
blockHeight = 32

settingsIcon = "settingsGear"


class viewerClass:
  def __init__(self, width, height, playerimg, levelimg):
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode([width, height])
    self.levelimg = pygame.image.load("assets/" + levelimg)
    self.playerimg = pygame.image.load("assets/" + playerimg)
  
  def adjustimg(self, img):
    filename = pygame.image.load("assets/"+ img)
    pygame.transform.scale(filename, (500, 350))
    
  def repaint(self, x, y):
    self.screen.fill("white")

    self.screen.blit(self.levelimg, (0, 0))
    self.screen.blit(self.playerimg, (self.width / 2 - 32, self.height / 2 - 32))

    # Print to screen
    pygame.display.flip
