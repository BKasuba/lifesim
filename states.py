from typing import Iterable

class States():
    def __init__(self,
                 bodies: Iterable,
                 ):
        self.bodies = bodies
    def wander(self):
        #iterate through each body and see if another body is nearby. Body could be anything, creature, food etc
        for i in range(len(self.bodies)):
            pass