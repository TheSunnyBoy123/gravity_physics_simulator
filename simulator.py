from object import Object
from system import System
import time as time
from turtle import *
from constants import *

obj_1 = Object(Sun, 0, 0, 0, 0)
obj_2 = Object(Earth, 1*AU, 0, 0, 3*10**4)

array = [obj_1, obj_2]

system = System(array)
turtle_1 = Turtle()
turtle_2 = Turtle()

turtle_1.shape("square")
turtle_2.shape("circle")

turtle_1.up()
turtle_2.up()

turtle_1.goto((obj_1.x/AU*100, obj_1.y/AU*100))
turtle_2.goto((obj_2.x/AU*100, obj_2.y/AU*100))

turtle_1.down()
turtle_2.down()

i=0
while True:
    print(i)
    i += dt
    obj_1.update(system.force(obj_1.id))
    obj_2.update(system.force(obj_2.id))
    turtle_1.goto((obj_1.x/AU*100, obj_1.y/AU*100))
    turtle_2.goto((obj_2.x/AU*100, obj_2.y/AU*100))
    # time.sleep(1)
    