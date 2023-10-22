from math import pi


class Circle:
    def __init__(self, radius_circl):
        if radius_circl < 0:
            raise ValueError("Радиус должен быть положительным!")
        self.radius_circl = radius_circl

    def calculate_square(self):
        area = pi * self.radius_circl ** 2
        return round(area, 3)  # округляем при помощи round

    def calculate_length(self):
        length1 = 2 * pi * self.radius_circl
        return round(length1, 3)


try:
    radius_circl = int(input("Введите радиус круга: "))
    circl = Circle(radius_circl)
    square = circl.calculate_square()
    length = circl.calculate_length()
    print(f"Площадь круга: {square}")
    print(f"Длина круга: {length}")

except ValueError as e:
    print(f"Ошибка: {e}")
