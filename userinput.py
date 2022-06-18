import keyboard
import pygame
import sys

clock = pygame.time.Clock()


class InputClass:
    def __init__(self, vc, sc):
        self.vc = vc
        self.sc = sc
        self.currentDir = 4

    def getkeydown(self):
        self.sc.setSpeed(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keyboard.is_pressed("q"):
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if self.currentDir <= 6:
                        self.currentDir += 1
                    else:
                        self.currentDir = 0
                if event.key == pygame.K_a:
                    if self.currentDir >= 1:
                        self.currentDir -= 1
                    else:
                        self.currentDir = 7
            if keyboard.is_pressed("s"):
                if keyboard.is_pressed("shift"):
                    self.sc.setSpeed(-2)
                else:
                    self.sc.setSpeed(-4)
                    self.sc.playersheet = "playersheet"
            else:
                self.sc.playersheet = "idlesheet"
            if keyboard.is_pressed("w"):
                if keyboard.is_pressed("shift"):
                    self.sc.setSpeed(2)
                else:
                    self.sc.setSpeed(4)
                    self.sc.playersheet = "playersheet"
            else:
                self.sc.playersheet = "idlesheet"
            self.sc.setDirection(self.currentDir)
        self.vc.repaint()
        clock.tick(18)
