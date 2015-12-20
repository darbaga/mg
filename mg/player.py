from pyglet.window import key

class Player(object):
    """The player class
    Represents the player. Has bunch of functions to do bunch of stuff.
    """

    def __init__(self, Map):
        self.Map = Map
        self.position = (0, 0)

        self.has_moved=False
        self.move_counter=20

    def move(self, coords):
        if self.Map.get_tile(coords).impassable and not self.has_moved:
            self.Map.get_tile(coords).collide(self)
            self.has_moved = True
            self.move_counter=15
        elif self.Map.get_tile(coords).impassable != True and not self.has_moved:
            self.Map.get_tile(coords).collide(self)
            self.position = coords
            self.has_moved=True
            self.move_counter=15

    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.move((self.position[0]+1, self.position[1]))
        elif symbol == key.LEFT:
            self.move((self.position[0]-1, self.position[1]))
        elif symbol == key.UP:
            self.move((self.position[0], self.position[1]+1))
        elif symbol == key.DOWN:
            self.move((self.position[0], self.position[1]-1))
        elif symbol==key.C:
            print(self.position)
    def update(self, dt):
        if self.move_counter>0:
            self.move_counter-=1
        if self.has_moved==True and self.move_counter==0:
            self.has_moved=False
            self.move_counter=20
