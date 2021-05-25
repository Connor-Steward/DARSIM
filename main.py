from vpython import *
from Car import *

# Set canvas size
scene.width = 350
scene.height = 300
scene.range = 1.3
scene.title = "Widgets (buttons, etc.)\n"


scene.width = 350
scene.height = 300
scene.range = 1.3
# Is animation running
running = True

# Func to start and pause animation
def Run(b):
    global running
    running = not running
    if running:
        b.text = "Pause"
    else:
        b.text = "Run"

# Button that triggers Run()
button(text="Pause", pos=scene.title_anchor, bind=Run)

# Ojbects

# TODO: Move objects to Class Car
# box_object = box(visible=True, length=0.30, height=1, width=0.60)
box_object = Car()
#cone_object = cone(visible=False, radius=0.5)
#pyramid_object = pyramid(visible=False)
cylinder_object = cylinder(visible=False, radius=0.5)

# Color
col = color.cyan
currentobject = box_object
currentobject.color = col


def Color(c):
    global col
    if col.equals(color.cyan):  # change to red
        currentobject.color = col = color.red
        c.text = "<b>Cyan</b>"
        c.color = color.cyan
        c.background = color.red
        r1.checked = False
        r2.checked = True
    else:  # change to cyan
        currentobject.color = col = color.cyan
        c.text = "<b>Red</b>"
        c.color = color.red
        c.background = color.cyan
        r1.checked = True
        r2.checked = False

# Click button to change colour
cbutton = button(text='<b>Red</b>', color=color.red, background=color.cyan, pos=scene.title_anchor, bind=Color)

# Caption on screen
scene.caption = "Vary the rotation speed: \n\n"

# Func to set speed of rotation
def setspeed(s):
    wt.text = '{:1.2f}'.format(s.value)

# Generate slider bar and bind to setspeed()
sl = slider(min=0.3, max=3, value=1.5, length=220, bind=setspeed, right=15)
wt = wtext(text='{:1.2f}'.format(sl.value))

# Caption on screen
scene.append_to_caption(' radians/s\n')

# Radio button 1 for Cyan - default
r1 = radio(bind=Color, checked=True, text='Cyan')

scene.append_to_caption('       ')

# # Func to change shape on screen
# def M(m):
#     global col, currentobject
#     op = currentobject.opacity
#     currentaxis = currentobject.axis
#     currentobject.visible = False
#     val = m.selected
#     if val == "box":
#         currentobject = box_object
#     elif val == "cone":
#         currentobject = cone_object
#     elif val == "pyramid":
#         currentobject = pyramid_object
#     elif val == "cylinder":
#         currentobject = cylinder_object
#     currentobject.color = col
#     currentobject.axis = currentaxis
#     currentobject.visible = True
#     currentobject.opacity = op

# Bind shape change to dropdown menu
# menu(choices=['Choose an object', 'box', 'cone', 'pyramid', 'cylinder'], index=0, bind=M)

scene.append_to_caption('\n')

# Radio button 2 - red
r2 = radio(bind=Color, text='Red')

scene.append_to_caption('         ')


def transparency(b):
    if b.checked:
        currentobject.opacity = 0.5
    else:
        currentobject.opacity = 1


checkbox(bind=transparency, text='Transparent')


#TODO this Spins the car, change .car_body to car compound object when created

# dt = 0.1
# while True:
#     rate(1 / dt)
#     if running:
#         currentobject.car_body.rotate(angle=sl.value * dt, axis=vector(0, 1, 0))


dt = 0.1
while True:
    rate(1 / dt)
    if running:
        currentobject.finished_car.rotate(angle=sl.value * dt, axis=vector(0, 1, 0))