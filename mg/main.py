import pyglet

import libaudioverse

import bot
from map import Map, Tile
from player import Player
from sound import SoundLoader

libaudioverse.initialize()
sim=libaudioverse.Simulation()
sim.set_output_device(-1)

Window = pyglet.window.Window()

loader=SoundLoader(sim)

default_tile=Tile(sound=loader.load_sound('footstep'))
impassable_tile=lambda: Tile(sound=loader.load_sound('impassable'), impassable=True)# need lambda for defaultdict, see map.py

#Map = Map(x=10, y=10, default_tile=default_tile, impassable_tile=impassable_tile)
Map=Map(default_tile=Tile(sound=loader.load_sound('impassable'), impassable=True), impassable_tile=lambda: Tile(sound=loader.load_sound('impassable'), impassable=True))
bot.do(Map)
Player = Player(Map)

Window.push_handlers(Player)

if __name__=='__main__':
    pyglet.clock.schedule_interval(Player.update, 1.0/60)
    pyglet.app.run()
