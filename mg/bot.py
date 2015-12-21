import random
from map import Tile
import libaudioverse
libaudioverse.initialize()
s=libaudioverse.Simulation()
s.set_output_device(-1)
from sound import SoundLoader
loader=SoundLoader(s)
class Bot(object):
    def __init__(self, map):
        self.map = map
        self.position=(0, 0)
    def execute(self):
        choice=random.randint(1, 4)
        if choice==1:
            self.map[(self.position[0]-1, self.position[1])]=Tile(sound=loader.load_sound('footstep'))
            self.position=(self.position[0]-1, self.position[1])
        elif choice==2:
            self.map[(self.position[0]+1, self.position[1])]=Tile(sound=loader.load_sound('footstep'))
            self.position=(self.position[0]+1, self.position[1])
        elif choice==3:
            self.map[(self.position[0], self.position[1]+1)]=Tile(sound=loader.load_sound('footstep'))
            self.position=(self.position[0], self.position[1]+1)
        elif choice==4:
            self.map[(self.position[0], self.position[1]-1)]=Tile(sound=loader.load_sound('footstep'))
            self.position=(self.position[0], self.position[1]-1)

def do(map):
    b1=Bot(map)
    b2=Bot(map)
    b3=Bot(map)
    b4=Bot(map)
    for i in range(100):
        b1.execute()
        b2.execute()
        b3.execute()
        b4.execute()
    return map