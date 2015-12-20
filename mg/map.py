"""The map class.
Implements tiles and the map singleton, nothing too fansy.
"""

from collections import defaultdict

class Tile(object):
    """The tile class.
    Tiles are conceptually the most basic objects in the game.
    """

    def __init__(self, sound, impassable=False):
        """Arguments:
          Sound: A sound object
          Impassable (True or false): if the tile is passable
        Returns a new class instance.
        """
        self.sound = sound
        self.impassable = impassable

    def collide(self):
        """Called when something touches the tile.
        Generally supposed to be called with super (when subclassing the Tile class)
        """
        self.sound.play()

class Map(object):
    """The map class.
    The container that holds all level data.
    Generally a single conceptual "level" will only have one map instance.
    """

    def __init__(self, x, y):
        """Args:
          x, y: The maximum length before walls appear.
        """
        self.x = x
        self.y = y

        self._map = defaultdict(lambda: Tile(sound='impassable', impassable=True))
        self._populate_map()

    def _populate_map(self):
        for i in range(self.x):
            for j in range(self.y):
                self._map[(i, j)] = Tile(sound='footstep')
    def get_tile(self, coordinates=(0, 0)):
        """Get the tile from the map
        Args:
          coordinates: Coordinates must be a tuple of x, y integers.
        """
        return self._map[coordinates]
