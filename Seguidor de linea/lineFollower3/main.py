#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, InfraredSensor)
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
mA = Motor(Port.A)
mD = Motor(Port.D)
lS = ColorSensor(Port.S1)

while True:
    reflejo = lS.reflection()

    if reflejo > umbral:
        mA.run(200)
        mD.brake()
    else:
        mA.brake()
        mD.run(200)

    wait(10)