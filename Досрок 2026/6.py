from turtle import *

left(90)
c = 30
tracer(0)
screensize(10_000, 10_000)

right(315)
for x in range(7):
    fd(12*c)
    rt(45)
    fd(6*c)
    rt(135)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * c, y * c)
        dot(5, 'pink')

done()