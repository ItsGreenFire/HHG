import pygame

clock = pygame.time.Clock()

class PlayerClass(pygame.sprite.Sprite):
    def __init__(self, playersheet, x, y, frames, screen):
        super().__init__()

        self.frames = frames
        self.index = 0
        self.screen = screen

        self.playersheet = playersheet
        self.currentx = x
        self.currenty = y

    def checkDirection(self, key, moving):
        directions = {0: "r",
                      45: "tr",
                      90: "t",
                      135: "tl",
                      180: "l",
                      225: "bl",
                      205: "b",
                      315: "br"}

        rd = (0, 45, 90, 205, 315)

        '''if key in rd: self.img = pygame.image.load("assets/" + "player_" + directions[key] + ".png") else: 
        self.img = pygame.transform.flip(pygame.image.load("assets/" + "player_" + directions[key] + ".png"), False, 
        True) '''
        self.drawplayer(directions[key], 10, 10, 32, 32, moving)

    def drawplayer(self, dir, x, y, w, h, moving):
        pimg = pygame.image.load("assets/" + self.playersheet + ".png")

        self.screen.blit(pimg, (100, 100))
        if moving:
            if self.index > self.frames:
                self.index = 0

            xPos = (self.index % 5) * w
            yPos = (self.index // 5) * h
            self.screen.blit(pimg, (x, y), (xPos, yPos, w, h))

            self.index = self.index + 1
            clock.tick(12)
        # print("hello")
        pygame.display.flip()

    def move(self, dir):
        pass
