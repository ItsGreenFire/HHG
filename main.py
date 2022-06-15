import sys

import keyboard
import pygame
from screeninfo import get_monitors

from sprites import SpriteClass
from viewer import ViewerClass

for monitor in get_monitors():
    pass

clock = pygame.time.Clock()

# Pygame
pygame.init()
pygame.display.set_caption("Horrific Horrors", "HH")
pygame.display.set_icon(pygame.image.load('assets/settingsGear.png'))

# Variables
running = True
pressed = pygame.key.get_pressed()
currentDir = 4


# Classes
vc = ViewerClass(1280, 720, "background.jpg")
sc = SpriteClass("playerSheet", 400, 100, 3, 8)
# pc.checkDirection(180)

if __name__ == '__main__':
    pass

    vc.add_sprite(sc)
    vc.repaint()

# ============================

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if keyboard.is_pressed("q"):
            sys.exit(0)

        if keyboard.is_pressed("w"):
            if keyboard.is_pressed("shift"):
                sc.setSpeed(5)
            else:
                sc.setSpeed(10)
        if keyboard.is_pressed("s"):
            if keyboard.is_pressed("shift"):
                sc.setSpeed(-5)
            else:
                sc.setSpeed(-10)
        if keyboard.is_pressed("a"):
            if currentDir >= 1:
                currentDir -= 1
            else:
                currentDir = 7
            sc.setDirection(currentDir)
        if keyboard.is_pressed("d"):
            if currentDir <= 6:
                currentDir += 1
            else:
                currentDir = 0
            sc.setDirection(currentDir)
    # TODO: Make player stop when no key is down
    '''
        if not any(pygame.key.get_pressed()):
            sc.setDirection(currentDir)
            sc.setSpeed(0)
    '''
    vc.repaint()
    clock.tick(18)
