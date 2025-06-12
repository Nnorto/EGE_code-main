from turtle import *

c = 30
screensize(10_000, 10_000)
left(90)
tracer(0)

for x in range(2):
    fd(3*c)
    rt(90)
    fd(20*c)
    rt(90)

up()
back(8*c)
rt(90)
fd(9*c)
lt(90)
down()

for x in range(2):
    fd(16*c)
    rt(90)
    fd(8*c)
    rt(90)

up()
for x in range(-52, 52):
    for y in range(-52, 52):
        goto(x*c, y*c)
        dot(5, 'blue')

update()
done()