from turtle import *
tracer(3) # самая большая скорость
screensize(3000, 3000) # ползунки
left(90) # поворачиваем черепаху вдоль оси у
c = 25 # делаем рисунок больше

# алгоритм из задания
for x in range(9):
    fd(22*c)
    rt(90)
    fd(6*c)
    rt(90)
up()
fd(1*c)
rt(90)
fd(5*c)
lt(90)
down()
for x in range(9):
    fd(53 * c)
    rt(90)
    fd(75 * c)
    rt(90)
# алгоритм для точек
up() # поднять хвост
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*c, y*c) # перемещаем черепаху на  x y
        dot(5, 'red') # точка

update() # для   tracer(0)
exitonclick() # для пайчарма