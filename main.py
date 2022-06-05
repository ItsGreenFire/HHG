import pygame
import sys
from viewer import viewerClass
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

vc = viewerClass(monitor.width - 150, monitor.height - 75, "settingsGear.png",
                 "background.jpg")

# Update Screen And Draw Player/Level
vc.repaint(100, 100)

if __name__ == '__main__':
    pass

# ============================

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if pressed[pygame.K_q]:
            sys.exit(0)
