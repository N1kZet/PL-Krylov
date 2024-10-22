# 2
import math


def distance(x1, y1, x2, y2):  # Находим координаты
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find_max_distanc(X, Y, Z, P):  # Находим макс дистанцию
    max_distance = 0
    max_point = []

    for i in [X, Y, Z, P]:
        for j in [X, Y, Z, P]:
            if i != j:
                dist = distance(i[0], j[0], i[1], j[1])
                if dist > max_distance:
                    max_distance = dist
                    max_point = [i, j]
    return max_distance, max_point


X = (float(input("Введите x1 для точки X: ")), float(input("Введите x2 для точки X: ")))
Y = (float(input("Введите y1 для точки Y: ")), float(input("Введите y2 для точки Y: ")))
Z = (float(input("Введите z1 для точки Z: ")), float(input("Введите z2 для точки Z: ")))
P = (float(input("Введите p1 для точки P: ")), float(input("Введите p2 для точки P: ")))

max_distance, max_point = find_max_distanc(X, Y, Z, P)

print(f"Максимальное расстояние: {max_distance}")
print(f"Точки, находящиеся на максимальном расстоянии: {max_point}")
