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
shiftDown = False

# Classes
vc = ViewerClass(1280, 720, "background.jpg")
sc = SpriteClass("playerSheet", 400, 100, 3, 8)
# pc.checkDirection(180)

if __name__ == '__main__':
    pass

    vc.add_sprite(sc)

# ============================x

while running:

    vc.repaint()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if not any(pygame.key.get_pressed()):
            sc.setDirection(4)
            sc.setSpeed(0)
            shiftDown = False
        else:
            if keyboard.is_pressed("q"):
                sys.exit(0)
            if keyboard.is_pressed("w"):
                sc.setDirection(0)
                sc.setSpeed(10)
            if keyboard.is_pressed("a"):
                sc.setDirection(6)
                sc.setSpeed(10)
            if keyboard.is_pressed("s"):
                sc.setDirection(4)
                sc.setSpeed(10)
            if keyboard.is_pressed("d"):
                sc.setDirection(2)
                sc.setSpeed(10)
            if keyboard.is_pressed("shift"):
                sc.setSpeed(5)
                shiftDown = True

    vc.repaint()
    if shiftDown:
        clock.tick(10)
    else:
        clock.tick(18)
