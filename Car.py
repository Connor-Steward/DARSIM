from vpython import *

class Car:
    def __init__(self):
        self.car_body = box(visible=True, color=color.cyan, length=0.60, height=1, width=0.30,)
        self.car_w1 = cylinder(visible=True, radius=0.08, length=0.50, height=0.8, width=0.60, color=color.red,
                               pos=vector(0, 0, 0))
        self.finished_car = compound([self.car_body, self.car_w1])


