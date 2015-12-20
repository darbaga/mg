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

    def __init__(self, x=0, y=0, map_dict=None):
        """Args:
          x, y: The maximum length before walls appear.
          map_dict: An externally supplied map dictionary.
        """
        self.x = x
        self.y = y

        if not map_dict:
            self._map = defaultdict(lambda: Tile(sound='impassable', impassable=True))
            self._populate_map()
        else:
            self._map = map_dict

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
