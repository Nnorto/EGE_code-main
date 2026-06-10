from math import dist
from turtle import *

tracer(0)
c = 1
left(90)
screensize(10_000, 10_000)
a = position()
dot(10, 'blue')

for x in range(9):
    fd(18*c)
    rt(72)
b = position()
print(dist(a, b))
dot(10, 'pink')

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * c, y *c)
        dot(3, 'red')

update()
done()