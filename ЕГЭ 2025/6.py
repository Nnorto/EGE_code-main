from turtle import *
lt(90)
screensize(10_000, 10_000)
tracer(0)
c = 30

for x in range(3):
    fd(27*c)
    rt(90)
    fd(12*c)
    rt(90)
up()
fd(4*c)
rt(90)
fd(6*c)
lt(90)
down()
for x in range(4):
    fd(83*c)
    rt(90)
    fd(77*c)
    rt(90)

up()
for x in range(-52, 52):
    for y in range(-52, 52):
        goto(x*c, y*c)
        dot(5, 'blue')

update()
done()