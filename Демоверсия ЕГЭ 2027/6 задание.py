from turtle import *
tracer(0)
c = 30
screensize(10000, 10000)
left(90)

for x in range(6):
    fd(24*c)
    rt(90)
    fd(30 * c)
    rt(90)
up()
fd(2*c)
rt(90)
fd(10 * c)
lt(90)
down()
for x in range(6):
    fd(75*c)
    rt(90)
    fd(71 * c)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*c, y*c)
        dot(5, 'red')
update()
done()