from vpython import *

class Car:
    def __init__(self):
        #self.pos = pos
        #self.axis = axis
        #self.radius = radius

        self.car_model = box(visible=True, color=color.cyan,)

    def rotate(self):
        dt = 0.01
        rotate(angle=1.5 * dt, axis=vector(0, 1, 0))

