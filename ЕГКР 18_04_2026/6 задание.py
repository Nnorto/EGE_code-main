from turtle import *

lt(90)
tracer(0)
c = 15
screensize(10_000, 10_000)

for x in range(6):
    fd(71 * c)
    rt(90)
    fd(73 * c)
    rt(90)
up()
fd(18 * c)
rt(90)
fd(22 * c)
lt(90)
down()

for x in range(6):
    fd(45 * c)
    rt(90)
    fd(58 * c)
    rt(90)

up()
for x in range(-30, 100):
    for y in range(-30, 100):
        goto(x * c, y * c)
        dot(5, 'blue')

done()
