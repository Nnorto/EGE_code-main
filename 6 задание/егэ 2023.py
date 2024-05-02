from turtle import *
const = 30
tracer(0)
lt(90)
screensize(2000, 2000)

for i in range(2):
    fd(14*const)
    rt(90)
    fd(10*const)
    rt(90)

up()
fd(8*const)
rt(90)
bk(4*const)
lt(90)
down()

for i in range(2):
    fd(9*const)
    rt(90)
    fd(8*const)
    rt(90)


up()
for x in range(-20, 20):
    for y in range(-20, 30):
        goto(x*const, y*const)
        dot(3, "blue")

update()
exitonclick()