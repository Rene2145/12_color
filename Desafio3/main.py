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
contador = 0
linea_negra = False

for i in range(750):
    
    mA.run(100)
    mD.run(100)

    color_detectado = color_sensor.color()

    if color_detectado == Color.BLACK and not linea_negra:
        contador = contador + 1
        linea_negra = True
    elif color_detectado != Color.BLACK:
        linea_negra = False
        ev3.screen.clear()
        ev3.screen.print("Contador:", contador)
        wait(200)

mA.brake()
mD.brake()
