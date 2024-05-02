from turtle import *
from math import *
const = 30
tracer(0)
lt(90)
screensize(2000, 2000)
"""
В начальный момент Черепаха находится в начале координат,
 её голова направлена вдоль положительного
  направления оси ординат, хвост поднят. 
Направо 30 Вперёд 4 Направо 330
Опустить хвост
Вперёд 4 Направо 90 Вперёд 7 Направо 45 Вперёд 4sqrt2
Направо 135 Вперёд 11
"""
up()
rt(30)
fd(4*const)
rt(330)
down()
fd(4*const)
rt(90)
fd(7*const)
rt(45)
fd(4*sqrt(2)*const)
rt(135)
fd(11*const)


up()
for x in range(-20, 20):
    for y in range(-20, 30):
        goto(x*const, y*const)
        dot(3, "blue")

update()
exitonclick()