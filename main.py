from random import random
from turtle import *


def oporno(cluster):
    maxx = -10**10
    maxy = -10**10
    minx = 10**10
    miny = 10**10
    verx, niz, levo, pravo = 0, 0, 0, 0
    for p in cluster:
        x, y = p
        if minx > x:
            levo = p
            minx = x
        if maxx < x:
            pravo = p
            maxx = x
        if miny > y:
            niz = p
            miny = y
        if maxy < y:
            verx = p
            maxy = y
    return [verx, niz, levo, pravo]
a = [[6, 8], [-1, 7], [-4, 9], [3, 2], [7, 7], [2, 10]]
tochki = [oporno(a)]

tracer(0)
up()
c = 50
screensize(10_000, 10_000)
for x, y in a:
    color = random(), random(), random()
    goto(x * c, y * c)
    dot(5, color)
for p in tochki:
    color = random(), random(), random()
    for x,y in p:
        goto(x*c, y*c)
        dot(15, color)

goto(12796391, 123123123)
update()
done()