#  Copyright © 2016 Oh Jun Kwon. All rights reserved.

# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole

class Pulsator(Black_Hole):
    updates = 30
    
    def __init__(self,x,y):
        self._radius = 10
        Black_Hole.__init__(self,x,y)
        self._counter = 0
    
    def update(self, model):
        
        width, height = self.get_dimension()
        self._counter += 1
        
        all_eaten = Black_Hole.update(self, model)
        if all_eaten:
            self.change_dimension(1,1)
            self._counter = 0
            
        if self._counter == Pulsator.updates:
            self.change_dimension(-1, -1)
            self._counter = 0
             
        if width + height == 0:
            model.remove(self)
                
        return all_eaten
