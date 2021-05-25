from vpython import *

class Car:
    def __init__(self):
        self.car_body = box(visible=True, color=color.cyan, length=0.30, height=1, width=0.60)
        self.car_w1 = cylinder(visible=True, radius=0.8, length=0.10, height=1, width=0.60, color=color.red)
        self.finished_car = compound([self.car_body, self.car_w1])


