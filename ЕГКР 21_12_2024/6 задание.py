from turtle import *
tracer(0)
screensize(30000, 30000)
c = 30
left(90)

for x in range(8):
    fd(16 * c)
    rt(90)
    fd(22 * c)
    rt(90)
up()
fd(5*c)
rt(90)
fd(5*c)
lt(90)
down()
for x in range(8):
    fd(52 * c)
    rt(90)
    fd(77 * c)
    rt(90)

up()
for x in range(-52, 52):
    for y in range(-52, 52):
        goto(x*c, y*c)
        dot(3, 'blue')

update()
exitonclick()