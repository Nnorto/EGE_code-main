from turtle import *

tracer(0)
screensize(2000, 2000)
left(90)  #смотрим на ось y
const = 20
for x in range(2):
    forward(8 * const)
    right(90)
    forward(18 * const)
    right(90)
up()
forward(4 * const)
right(90)
forward(10 * const)
left(90)
down()
for x in range(2):
    forward(17 * const)
    right(90)
    forward(7 * const)
    right(90)

# рисуем точки
up()
for x in range(-20, 30):
    for y in range(-20, 35):
        goto(x * const, y * const)
        dot(3, 'red')

exitonclick()