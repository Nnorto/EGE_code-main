from turtle import *
tracer(0)
c = 30
screensize(10_000, 10_000)
lt(90)

for x in range(4):
    fd(28*c)
    rt(90)
    fd(26 * c)
    rt(90)
up()
fd(12*c)
rt(90)
fd(13 * c)
lt(90)
down()
for x in range(4):
    fd(67*c)
    rt(90)
    fd(76 * c)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * c, y * c)
        dot(3, 'red')
done()