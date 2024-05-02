from turtle import *
tracer(0)
screensize(1000, 1000)
c = 30
left(90)
rt(45)
for i in range(7):
    fd(5*c)
    rt(45)
    fd(10*c)
    rt(135)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*c, y*c)
        dot(3, "black")

update()
exitonclick()
