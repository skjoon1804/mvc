#  Copyright © 2016 Oh Jun Kwon. All rights reserved.

import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter

from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
balls = set()
object_name = None
once = False

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, balls, object_name
    running = False
    cycle_count = 0
    balls = set()
    object_name = None
    


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global running, once
    running = True
    once = True
    

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object_name
    object_name = kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    try:
        if object_name == 'Ball':
            balls.add(Ball(x,y))
        elif object_name == 'Floater':
            balls.add(Floater(x,y))
        elif object_name == 'Black_Hole':
            balls.add(Black_Hole(x,y))
        elif object_name == 'Pulsator':
            balls.add(Pulsator(x,y))
        elif object_name == 'Hunter':
            balls.add(Hunter(x,y))  
        elif object_name == 'Special':
            balls.add(Special(x,y))
  
        elif object_name == 'Remove':
            for i in find(lambda a: a.contains((x,y))):
                balls.remove(i)      
        
    except:
        pass



#add simulton s to the simulation
def add(s):
    global balls
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global balls
    balls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    sim_set = set()
    for i in balls:
        if p(i):
            sim_set.add(i)
    return sim_set
    
    


#call update for every simulton in the simulation
def update_all():
    global running, cycle_count,balls, once, world
    if running:
        cycle_count += 1 
        
        for b in balls.copy():
            b.update(model)
            
        if once:
            running=False
            once = False


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")

