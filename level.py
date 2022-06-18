class LevelClass:

    def __init__(self, level):
        self.level = level
        self.lfile = ("level_" + str(level) + ".png")

    def changelevel(self, num):
        self.level += num
        return self.lfile
