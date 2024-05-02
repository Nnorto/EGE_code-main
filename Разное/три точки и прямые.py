import tkinter as tk

def draw_line(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2)

root = tk.Tk()
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

x1, y1 = 10, 10
x2, y2 = 50, 50

x3, y3 = 25, 25

k1 = (y2 - y1) / (x2 - x1)
c1 = y1 - k1 * x1

k2 = -1 / k1
c2 = y3 - k2 * x3

print(f"Исходная прямая: y = {k1}x + {c1}")
print(f"Перпендикулярная прямая: y = {k2}x + {c2}")


# Конечные точки для исходной прямой
end_x1 = x1 + 50
end_y1 = k1 * end_x1 + c1

# Конечные точки для перпендикулярной прямой
end_x2 = x3 + 20
end_y2 = k2 * (end_x2 - x3) + y3

# Рисуем прямые на холсте
draw_line(canvas, x1, y1, end_x1, end_y1)
draw_line(canvas, x3, y3, end_x2, end_y2)

root.mainloop()
