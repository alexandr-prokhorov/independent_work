# Задача 8.1
# Используя понятие множественного наследования,
# разработайте класс «Окружность, вписанная в квадрат».
# Поля:
# для окружности - радиус;
# для квадрата - сторона.
# Методы:
# для окружности длина и площадь;
# для квадрата сторона и площадь.

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square:

    def __init__(self, side):
        self.side = side

    def perimetr(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2


class CircleInSquare(Circle, Square):

    def __init__(self, side):
        self.side = side

        Square.__init__(self, side)
        Circle.__init__(self, side / 2)

    def display(self):
        return (f"Окружность с радиусом {self.radius}, длиной {self.circumference():.2f}, "
                f"площадью {self.area():.2f}, вписана в Квадрат со стороной {self.side}, "
                f"площадью {Square.area(self):.2f}")


print()
figure = CircleInSquare(10)
print(figure.display())
