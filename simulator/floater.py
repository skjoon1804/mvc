#  Copyright © 2016 Oh Jun Kwon. All rights reserved.

# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    def __init__(self, x,y):
        self._radius = 5
        Prey.__init__(self, x, y, self._radius*2, self._radius*2, 0,5)
        self.randomize_angle()

    def update(self, model):
        if round(random()*10) < 4:
            update_speed = (random()- 0.5) + self.get_speed()
            if 3<update_speed<7:  
                self.set_velocity(update_speed, (random() - 0.5)+self.get_angle())
            else:
                self.set_velocity(self.get_speed(), (random() - 0.5)+self.get_angle())      
        self.move()
    

    def display(self, canvas):
        canvas.create_oval(self._x - self._radius, self._y - self._radius, self._x + self._radius, self._y + self._radius, fill = 'red')
    

        
        