import pygame

clock = pygame.time.Clock()


class SpriteClass(pygame.sprite.Sprite):
    def __init__(self, playersheet, x, y, scale, frames):
        super().__init__()

        self.frames = frames
        self.index = 0
        self.direction = 4
        self.speed = 0
        self.playersheet = playersheet
        self.currentx = x
        self.currenty = y
        self.scale = scale

    def setDirection(self, d):
        self.direction = d

    def setSpeed(self, speed):
        self.speed = speed

    def move(self):
        xoffsets = [0, self.speed, self.speed, self.speed, 0, -self.speed, -self.speed, -self.speed]
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
