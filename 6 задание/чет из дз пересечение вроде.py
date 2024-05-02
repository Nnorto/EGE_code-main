from turtle import *
screensize(5000, 1000)
tracer(0)
c = 25
bgcolor('gray')
color('yellow')
pensize(3)
left(90)

for x in range(2):
    fd(7*c)
    rt(90)
    fd(20 * c)
    rt(90)
up()
fd(3*c)
rt(90)
fd(7*c)
lt(90)
down()
for x in range(4):
    rt(90)
    fd(7*c)



up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*c, y*c)
        dot(3, 'black')



update()
exitonclick()
