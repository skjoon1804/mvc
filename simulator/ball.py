#  Copyright © 2016 Oh Jun Kwon. All rights reserved.

# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    def __init__(self,x,y):
        self._radius = 5
        self._x, self._y = x, y
        Prey.__init__(self, self._x, self._y, self._radius*2, self._radius*2, 0,5)
        self.randomize_angle()
    
    def display(self, canvas):
        canvas.create_oval(self._x - self._radius, self._y - self._radius, self._x + self._radius, self._y + self._radius, fill='blue')

    def update(self, model):
        self.move()
        