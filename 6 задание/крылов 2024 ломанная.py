from turtle import *
k = 20
tracer(0)
screensize(3000, 3000)
left(90)

for x in range(3):
    down()
    for i in range(2):
        fd(10*k)
        rt(90)
        fd(10 * k)
        rt(90)
    up()
    fd(10 * k)
    rt(90)
    fd(5 * k)
    lt(90)


up()
for x in range(-30, 30):
    for y in range(-30, 50):
        goto(x*k, y*k)
        dot(4, "pink")


update()
exitonclick()