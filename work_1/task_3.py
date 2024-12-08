# Создать базовый класс «Домашнее животное» и производные
# классы «Собака», «Кошка», «Попугай», «Хомяк». С помощью
# конструктора установить имя каждого животного и его
# характеристики. Реализуйте для каждого из классов методы:
# get_sound — издает звук животного (пишем текстом в
# консоль);
# get_name — отображает имя животного;
# get_type — отображает название его подвида;
# Поля у классов должны быть такие чтобы их можно корректно
# было передать в методы также поля должны быть
# защищены.

class Pet:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species


class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Собака")
        self.__breed = breed

    def get_sound(self):
        print("Гав!")

    def get_breed(self):
        return self.__breed


class Cat(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Кошка")
        self.__breed = breed

    def get_sound(self):
        print("Мяу")

    def get_breed(self):
        return self.__breed


class Parrot(Pet):
    def __init__(self, name, color):
        super().__init__(name, "Попугай")
        self.__color = color

    def get_sound(self):
        print("Кар-Кар")

    def get_color(self):
        return self.__color


class Hamster(Pet):
    def __init__(self, name, color):
        super().__init__(name, "Хомяк")
        self.__color = color

    def get_sound(self):
        print("Шипит")

    def get_size(self):
        return self.__color


dog = Dog(name="Дик", breed="Немецкая овчарка")
cat = Cat(name="Маркус", breed="Шотландец")
parrot = Parrot(name="Кеша", color="Синий")
hamster = Hamster(name="Чип", color="Серый")

print(f"Имя собаки: {dog.get_name()}, Порода: {dog.get_breed()}")
dog.get_sound()
print(f"Имя кошки: {cat.get_name()}, Порода: {cat.get_breed()}")
cat.get_sound()
print(f"Имя попугая: {parrot.get_name()}, Цвет: {parrot.get_color()}")
parrot.get_sound()
print(f"Имя хомяка: {hamster.get_name()}, Цвет: {hamster.get_size()}")
hamster.get_sound()
