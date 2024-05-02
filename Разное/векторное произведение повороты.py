def count_left_turns(road):
    left_turns = 0

    for i in range(len(road) - 2):
        x1, y1 = road[i]
        x2, y2 = road[i+1]
        x3, y3 = road[i+2]
        cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)

        if cross_product > 0:
            left_turns += 1

    return left_turns

# Определение массива точек
road = [(0, 0), (1, 2), (2, 1), (4, 4), (5, 2)]

# Вызов функции для подсчета количества левых поворотов
left_turns = count_left_turns(road)

print(f"Количество левых поворотов: {left_turns}")
