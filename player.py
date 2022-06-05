import pygame

class PlayerClass:
    def __init__(self, playerimg, x, y):
        self.img = "assets/" + playerimg
        self.currentx = x
        self.currenty = y

    def checkDirection(self, key):
        directions = {0: "r",
                      45: "tr",
                      90: "t",
                      135: "tl",
                      180: "l",
                      225: "bl",
                      205: "b",
                      315: "br"}

        self.img = "player_" + directions[key] + ".png"

    def loadPlayer(self, playerScreen):
        playerScreen.blit(self.img, ())

    def move(self, dir):
        if dir == 0:
            pass
        if dir == 1:
            pass
        if dir == 2:
            pass
        if dir == 3:
            pass


