# Используя механизм множественного наследования или
# композицию разработайте класс “Автомобиль”. Должны быть
# классы «Колеса», «Двигатель», «Двери». Требования к классам:
# 2 поля (атрибута) - они должны быть защищены
# ко всем полям написаны геттеры
# к 1 полю написан еще и сеттер

class Wheels:
    def __init__(self, type_wheels, size):
        self.__type_wheels = type_wheels
        self.__size = size

    def get_type_wheels(self):
        return self.__type_wheels

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if size > 0:
            self.__size = size
        else:
            raise ValueError("Размер должен быть положительным")


class Engine:
    def __init__(self, power, oil_type):
        self.__power = power
        self.__oil_type = oil_type

    def get_power(self):
        return self.__power

    def get_oil_type(self):
        return self.__oil_type


class Doors:
    def __init__(self, color, count):
        self.__color = color
        self.__count = count

    def get_color(self):
        return self.__color

    def get_count(self):
        return self.__count


class Car:
    def __init__(self, name, wheel_type_wheels, wheel_size, engine_power, engine_oil_type, doors_color, doors_count):
        self.name = name
        self.wheels = Wheels(wheel_type_wheels, wheel_size)
        self.wheels.set_size(wheel_size)
        self.engine = Engine(engine_power, engine_oil_type)
        self.doors = Doors(doors_color, doors_count)

    def display_info(self):
        return (
            f"Автомобиль '{self.name}' с {self.wheels.get_type_wheels()} колесами {self.wheels.get_size()} диаметра, "
            f"двигателем мощностью {self.engine.get_power()} л.с, c топливом типа {self.engine.get_oil_type()} "
            f"и дверьми количеством {self.doors.get_count()} шт. в цвете {self.doors.get_color()}.")


car = Car(name="Ford", wheel_type_wheels="шипованными", wheel_size=16, engine_power=120, engine_oil_type="ДТ",
          doors_color="белый", doors_count=4)
print()
print(car.display_info())
