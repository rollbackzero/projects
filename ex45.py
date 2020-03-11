from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):                 # This is a parent class 

    def start(self):
        exit(1)   

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene.map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()                   # defined current scene
        last_scene = self.scene_map.next_scene('finished')               # defined last scene

        while current_scene != last_scene:                               # perform a loop while current_scene is not equal to last_scene  
            next_scene_name = current_scene.enter()                      # the scene (via Map class opening_scene function)
            current_scene = self.scene_map.next_scene(next_scene_name)   # open/enter the scene (via Map class opening_scene function) 
        current.scene.enter()                                            # print out last scene



class Death(Scene):
    
    def enter(self):
        pass

class Chamber(Scene):

    def enter(self):
        pass

class ControlRoom(Scene):

    def enter(self):
        pass

class Basement(Scene):

    def enter(self):
        pass

class SecretRoom(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self):
        pass

    def opening_scene(self):
        pass

a_map = Map('chamber')
a_game = Engine(a_map)
a_game.play()

