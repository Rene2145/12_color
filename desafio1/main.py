#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Color, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S1)

while True:
    detected_color = color_sensor.color()

    ev3.screen.clear()

    if detected_color == Color.RED:
        ev3.screen.print("Color detectado:")
        ev3.screen.print("Rojo")   

        wait(2500)
        
    else:
        ev3.screen.print("Desconocido")

        wait(2500)