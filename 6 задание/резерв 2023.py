from turtle import *
const = 30
tracer(0)
lt(90)
screensize(2000, 2000)

rt(90)
for i in range(3):
    rt(45)
    fd(7*const)
    rt(45)
rt(315)
fd(7*const)
for i in range(2):
    rt(90)
    fd(7*const)


up()
for x in range(-20, 20):
    for y in range(-20, 30):
        goto(x*const, y*const)
        dot(3, "blue")

update()
exitonclick()