import pygame

clock = pygame.time.Clock()


class SpriteClass(pygame.sprite.Sprite):
    def __init__(self, playersheet, x, y, scale, frames):
        super().__init__()

        self.frames = frames
        self.index = 0
        self.direction = 0
        self.speed = 0
        self.playersheet = playersheet
        self.currentx = x
        self.currenty = y
        self.scale = scale

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

    def setDirection(self, d):
        self.direction = d

    def setSpeed(self, speed):
        self.speed = speed

    def move(self):
        xoffsets = [0,self.speed, self.speed, self.speed, 0, -self.speed, -self.speed, -self.speed]
        yoffsets = [-self.speed, -self.speed, 0, self.speed, self.speed, self.speed, 0, -self.speed]

        self.currentx += xoffsets[self.direction]
        self.currenty += yoffsets[self.direction]

    def drawSprite(self, screen):
        pimg = pygame.image.load("assets/" + self.playersheet + ".png")
        simg = pygame.transform.scale(pimg, (pimg.get_width() * self.scale, pimg.get_height() * self.scale))
        if self.index > self.frames:
            self.index = 0

        sizerect = 32 * self.scale
        xPos = (self.index % 8) * sizerect
        yPos = self.direction * sizerect
        self.move()
        screen.blit(simg, (self.currentx, self.currenty), (xPos, yPos, sizerect, sizerect))
        self.index += 1
        # screen.blit(simg, (100, 100))

    '''        if moving:
                if self.index > self.frames:
                    self.index = 0
    
                xPos = (self.index % 5) * w
                yPos = (self.index // 5) * h
                screen.blit(pimg, (x, y), (xPos, yPos, w, h))
    
                self.index = self.index + 1
                clock.tick(12)
            # print("hello")
            pygame.display.flip()
    '''
