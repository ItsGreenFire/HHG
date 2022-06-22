import json
import pygame


class FloorClass:

    def __init__(self, level, x, y):
        self.file = "floorplans/level_" + str(level) + ".txt"
        self.x = x
        self.y = y

    def read_file(self):
        f = open(self.file, "r")
        lines = f.readlines()
        y = self.y
        for line in lines:
            x = self.x
            for ch in line:
                if ch != "\n" and ch != " ":
                    return "assets/" + str(self.get_tiles(ch))
                x += 1
            y += 1

    def get_tiles(self, sym):
        j = open("floorplans/tiles.json")
        data = json.load(j)
        for tile in data["tiles"]:
            if tile["sym"] is not None:
                return tile["file"]
            else:
                print("Null JSON Char -> " + sym)
