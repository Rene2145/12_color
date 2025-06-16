#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Color, Port, Stop, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S1)
mA = Motor(Port.A)
mD = Motor(Port.D)

while True:
    
    if color_sensor.color() == Color.RED:
        ev3.screen.print("Color detectado:")
        ev3.screen.print("Rojo")
        break
    mA.run(300)
    mD.run(300)

mA.brake()
mD.brake()

wait(1000)

mA.run(-300)
mD.run(-300)

wait(1000)