import pygame
import sys
from viewer import ViewerClass
from player import PlayerClass
from level import levelClass

from screeninfo import get_monitors

for monitor in get_monitors():
    pass

# Pygame
pygame.init()
pygame.display.set_caption("Horrific Horrors", "HH")
pygame.display.set_icon(pygame.image.load('assets/settingsGear.png'))

# Variables
running = True
pressed = pygame.key.get_pressed()


# Classes

# lc = levelClass(400, 400)

vc = ViewerClass(monitor.width - 150, monitor.height - 75, "background.jpg")
pc = PlayerClass("settingsGear", 0, 0)
pc.checkDirection(180)
pc.loadPlayer(vc.getScreen())

print(monitor.width - 150, monitor.height - 75)

# Update Screen And Draw Player/Level
vc.repaint()

if __name__ == '__main__':
    pass

# ============================

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    if pressed[pygame.K_q]:
        sys.exit(0)
    if pressed[pygame.K_w]:
        pc.checkDirection(90)
        pc.move(0)

