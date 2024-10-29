from math import *
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def func(self,other):
        distance = sqrt(self.x**2 + self.y**2)-sqrt(other.x**2+other.y**2)
        return distance
    def __repr__(self):
        return f'Точка x: {self.x}, Точка y: {self.y}'

point1 = Point(int(input('Введите x: ')),int(input('Введите y: ')))
point2 = Point(int(input('Введите x: ')),int(input('Введите x: ')))
print(abs(point1.func(point2)))