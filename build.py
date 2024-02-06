import random
from typing import Iterable, Callable

def createHerd(
        species: Callable,
        number: int,
        colour: str,
        bodies: Iterable,
        windowWidth:int,
        windowHeight:int,
        travelPath: Iterable        
):
    group = []
    for i in range(number):
        new_body = species(colour, windowHeight = windowHeight, windowWidth = windowWidth)
        group.append(new_body)
        bodies.append(new_body)
    return group

class Carnivore():
    def __init__(self,
                  colour:str,
                  travelPath: Iterable = None,
                  x:int = None,
                  y:int = None,
                  windowWidth:int = None,
                  windowHeight:int = None
                  ):
        self.x = x or random.randint(1,windowWidth)
        self.y = y or random.randint(1,windowHeight)
        self.colour = colour
        self.speed = 3
        self.health = 10
        self.travelPath = travelPath

        