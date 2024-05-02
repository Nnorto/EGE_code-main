import matplotlib.pyplot as plt   # этот модуль нужно скачать это не встроенная библеотека
import numpy as np
import math
import sys
sys.setrecursionlimit(10000)
def circle(point, center, radius):
    # Функция для проверки, лежит ли точка на окружности
    epsilon = 0.005
    return abs(math.dist(point, center) - radius) < epsilon

def peres(start, s_end, center, radius, epsilon=0.005):
    x1, y1 = start
    x2, y2 = s_end

    # метод половинного деления
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    # Проверяем, лежат ли начальная и конечная точки отрезка на окружности
    if circle(start, center, radius):
        return [start]
    if circle(s_end, center, radius):
        return [s_end]

    if circle((mid_x, mid_y), center, radius):
        return [(mid_x, mid_y)]

    point1 = peres(start, (mid_x, mid_y), center, radius, epsilon)
    point2 = peres((mid_x, mid_y), s_end, center, radius, epsilon)

    return point1 + point2


start = (0, 0)
s_end = (0, 4)
start1 = (0, 0)
s_end1 = (4, 0)
center = (2, 2)
radius = 2


points_peres = peres(start, s_end, center, radius)
points_peres2 = peres(start1, s_end1, center, radius)
print("Точки пересечения:", points_peres)
print("Точки пересечения:", points_peres2)

# Нарисуем окружность
theta = np.linspace(0, 2*np.pi, 100)
x_circle = center[0] + radius * np.cos(theta)
y_circle = center[1] + radius * np.sin(theta)

plt.plot(x_circle, y_circle, label='Окружность')

# Нарисуем отрезок


# Отметим точки пересечения
for point in points_peres:
    plt.plot(point[0], point[1], 'bo')

plt.plot([-2, 4], [4, -2], 'r', label='Отрезок')
for point in points_peres2:
    plt.plot(point[0], point[1], 'bo')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Окружность и отрезок с их точками пересечения')
plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()
