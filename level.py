import numpy as np

class levelClass:

    def __init__(self, height, width):
        self.height = height
        self.width = width
#        self.world = np.full([height,width])

    def load(self, borderFile, posX, posY):
        f = open(borderFile, "r")
        lines = f.readlines()
        y = posY
        for line in lines:
            x = posX
            for ch in line:
                if ch != "\n" and ch != " ":
                    self.world[y][x] = ch
                x += 1
            y += 1

#    def save(self, borderFile, posX, posY, height, width):
#        f = open(borderFile, "w")
#        for y in range(posY, posY + height):
#            for x in range(posX, posX + width):
#                f.write(self.world[y][x])
#            f.write("\n")

    def perimeter(self, x, y, width, height, sym):
        for i in range(x, x+width):
            self.world[y][i] = sym
            self.world[y + height-1][i] = sym
        for i in range(y, y + height):
            self.world[i][x] = sym
            self.world[i][x+width-1] = sym

    def fill(self, x, y, width, height, sym):
        for i in range(x, x+width):
            for j in range(y, y + height):
                self.world[j][i] = sym
