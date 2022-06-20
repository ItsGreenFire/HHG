import pygame
from sprites import SpriteClass
from viewer import ViewerClass
from level import LevelClass
from userinput import InputClass

if __name__ == '__main__':
    pass

# Pygame
pygame.init()
pygame.display.set_caption("Horrific Horrors", "HH")
pygame.display.set_icon(pygame.image.load('assets/settingsGear.png'))

# Classes
vc = ViewerClass(1280, 720, "level_1.png")
sc = SpriteClass("playerSheet", 400, 100, 3, 8)
lc = LevelClass(1)
io = InputClass(vc, sc)

vc.add_sprite(sc)
# ============================
while True:
    io.getkeydown()
