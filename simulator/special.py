#  Copyright © 2016 Oh Jun Kwon. All rights reserved.

#glowing balls move in constant directions bouncing off the walls
#when those balls meet pray, they eat pray

from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton

from prey import Prey
import random


class Special(Pulsator,Mobile_Simulton):
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        width,height = self.get_dimension()
        
        Mobile_Simulton.__init__(self, x, y, width, height, 0, 5)
        self.randomize_angle()


    def color(self):
        return "#"+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]
    
        
    def display(self, canvas):
        canvas.create_oval(self._x-self._radius, self._y-self._radius, self._x+self._radius, self._y+self._radius, fill = self.color())

        
    def update(self,model):         
        for e in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(e.get_location()):   
                model.remove(e)
        self.move()
        












