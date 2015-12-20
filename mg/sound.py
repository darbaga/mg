"""The sound module
Has a Sound class which can be used as an abstraction for libaudioverse buffer nodes.
Also contains a sound cache.
"""
import os

import libaudioverse
import platform_utils.paths

SOUND_DIR = os.path.join(platform_utils.paths.embedded_data_path(), 'sounds')

class SoundLoader(object):

    def __init__(self, simulation):
        self.simulation = simulation
        self.cache = dict()

    def load_sound(self, key):
        #our sounds are ogg, so just add .ogg
        if key not in self.cache:
            b = libaudioverse.Buffer(self.simulation)
            b.load_from_file(os.path.join(SOUND_DIR, key+".ogg"))
            self.cache[key] = b
        b = self.cache[key]
        n = libaudioverse.BufferNode(self.simulation)
        n.buffer.value = b
        return Sound(n)

class Sound(object):

    def __init__(self, buffer_node):
        self.buffer_node = buffer_node

#    def stop(self):
#        self.buffer_node.state = libaudioverse.NodeStates.stop

    def is_playing(self):
        return self.buffer_node.state == libaudioverse.NodeStates.playing

    def play(self):
        #always set position to 0, then play
        self.buffer_node.connect_simulation(0)
        self.buffer_node.position = 0
        self.buffer_node.state = libaudioverse.NodeStates.playing
