from constants import *

class Object:
    count = 0
    def __init__(self, mass, x, y, v_x, v_y):
        self.mass = mass
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        Object.count += 1
        self.id = Object.count
    
    def update(self, force):
        acc = [0, 0]
        acc[0] = force[0]/self.mass
        acc[1] = force[1]/self.mass
        self.v_x += acc[0]*dt
        self.v_y += acc[1]*dt
        self.x += self.v_x*dt + 0.5*acc[0]*(dt**2)
        self.y += self.v_y*dt + 0.5*acc[1]*(dt**2)
        
    
