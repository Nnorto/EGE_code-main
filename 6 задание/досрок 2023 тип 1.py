from turtle import *
const = 30
tracer(0)
lt(90)
screensize(2000, 2000)


for i in range(7):
    fd(12 * const)
    rt(45)
    fd(6 * const)
    rt(135)





up()
for x in range(-20, 20):
    for y in range(-20, 30):
        goto(x*const, y*const)
        dot(3, "blue")

update()
exitonclick()