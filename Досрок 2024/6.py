from turtle import *
tracer(0)
left(90)
screensize(2000,2000)
const = 30
down()
for i in range(2):
    fd(13*const)
    rt(90)
    fd(18*const)
    rt(90)
up()
fd(5*const)
rt(90)
fd(9*const)
lt(90)
down()
for i in range(2):
    fd(11*const)
    rt(90)
    fd(7*const)
    rt(90)
up()
for x in range(-30,30):
    for y in range(-30,40):
        goto(x*const,y*const)
        dot(5,"red")
update()
exitonclick()