from turtle import *
tracer(0)
left(90)
screensize(3000, 3000)
const = 30

# алгоритм
for i in range(7):
    forward(10*const)
    right(120)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*const, y*const)
        dot(5, "red")

update()
exitonclick()