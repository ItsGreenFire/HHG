from sprites import SpriteClass
from viewer import ViewerClass
from floor import FloorClass
from userinput import InputClass

if __name__ == '__viewer__':
    pass

# Classes
fc = FloorClass(0, 100, 100)
vc = ViewerClass(1280, 720, fc.read_file())
sc = SpriteClass("playerSheet", 400, 100, 3, 8)
io = InputClass(vc, sc, fc)


vc.add_sprite(sc)
# ============================
while True:
    io.getkeydown()
