from turtle import *
screensize(3000, 3000)
tracer(0)
left(90)
c = 10
for x in range(9):
    fd(29 * c)
    rt(90)
    fd(17 * c)
    rt(90)

up()
fd(5 * c)
rt(90)
fd(1 * c)
lt(90)

down()
for x in range(9):
    fd(64 * c)
    rt(90)
    fd(48 * c)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * c, y * c)
        dot(3, 'red')

exitonclick()
update()
