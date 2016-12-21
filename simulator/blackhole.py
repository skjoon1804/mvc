#  Copyright © 2016 Oh Jun Kwon. All rights reserved.

# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    def __init__(self,x,y):
        self._radius = 10
        Simulton.__init__(self,x, y, self._radius*2, self._radius*2)
        self._width, self._height = self.get_dimension()
  
    def update(self,model):
        all_eaten = set()            
        for e in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(e.get_location()):   
                all_eaten.add(e)
                model.remove(e)

        return all_eaten

    def display(self, canvas):
        canvas.create_oval(self._x-self._width/2, self._y-self._height/2, self._x+self._width/2, self._y+self._height/2 , fill = 'black')
            
        

