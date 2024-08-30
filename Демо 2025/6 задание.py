from turtle import *
screensize(1000, 1000)
tracer(0)
left(90)
c = 20
for x in range(9):
    forward(22 * c)
    right(90)
    forward(6 * c)
    right(90)

up()
forward(1 * c)
rt(90)
fd(5 * c)
lt(90)

down()

for x in range(9):
    forward(53 * c)
    right(90)
    forward(75 * c)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 40):
        goto(x*c, y*c)
        dot(3, 'red')
update()
exitonclick()