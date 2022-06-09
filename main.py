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
vc = ViewerClass(monitor.width - 150, monitor.height - 75, "background.jpg", 8)
pc = PlayerClass("playerSheet", 100, 100, 8, vc.screen)
# pc.checkDirection(180)

if __name__ == '__main__':
    pass

    vc.repaint()
# ============================

while running:
    pc.checkDirection(45, True)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    if pressed[pygame.K_q]:
        sys.exit(0)
    if pressed[pygame.K_w]:
        pc.checkDirection(45, True)
