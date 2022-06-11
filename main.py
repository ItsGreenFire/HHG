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


# Classes
vc = ViewerClass(monitor.width - 150, monitor.height - 75, "background.jpg")
sc = SpriteClass("playerSheet", 400, 100, 3, 8)
sc2 = SpriteClass("playerSheet", 500, 300, 20, 8)
sc2.setDirection(2)
sc2.setSpeed(12)
# pc.checkDirection(180)

if __name__ == '__main__':
    pass

    vc.add_sprite(sc)
    vc.add_sprite(sc2)
    vc.repaint()

# ============================

while running:
    if sc2.currentx >= 550:
        sc2.setDirection(6)
    if sc2.currentx <= 100:
        sc2.setDirection(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if not any(pygame.key.get_pressed()):
            sc.setDirection(4)
            sc.setSpeed(0)
        else:
            if keyboard.is_pressed("q"):
                sys.exit(0)
            if keyboard.is_pressed("w"):
                sc.setDirection(0)
                sc.setSpeed(8)
            if keyboard.is_pressed("a"):
                sc.setDirection(6)
                sc.setSpeed(8)
            if keyboard.is_pressed("s"):
                sc.setDirection(4)
                sc.setSpeed(8)
            if keyboard.is_pressed("d"):
                sc.setDirection(2)
                sc.setSpeed(8)

    vc.repaint()
    clock.tick(24)
