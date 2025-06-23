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
distancia = 0
linea_negra = False

while contador < 9:
    
    mA.run(45)
    mD.run(45)

    color_detectado = color_sensor.color()

    if color_detectado == Color.BLACK:
        contador = contador + 1
        linea_negra = True
    elif color_detectado != Color.BLACK:
        linea_negra = False
        contador = 0
    if color >1:
        ev3.screen.clear()
        ev3.screen.print("Raya")
        wait(300)
    else
        ev3.screen.clear()
        ev3.screen.print("Punto")    
        wait(300)

mA.brake()
mD.brake()
