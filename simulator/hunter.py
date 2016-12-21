#  Copyright © 2016 Oh Jun Kwon. All rights reserved.

# A Hunter is both a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        self._width, self._height = self.get_dimension()
        Mobile_Simulton.__init__(self, x, y, self._width, self._height, 0, 5)
        self.randomize_angle()

        
    def update(self, model):
        list_food = []
        food_distance = []
        
        Pulsator.update(self, model)
        
        for e in model.find(lambda x: isinstance(x,Prey)):
            if 0<=self.distance(e.get_location()) <= 200:
                list_food.append(e)
        
        if list_food:
            for i in list_food:
                food_distance.append((self.distance(i.get_location()), i))
                
            food = (sorted(food_distance))[0][1]
            
            hunt_x, hunt_y = self.get_location()
            food_x, food_y = food.get_location()
            self.set_angle(atan2(food_y - hunt_y, food_x-hunt_x))
                 
        self.move()  
                
                
                
                
    
