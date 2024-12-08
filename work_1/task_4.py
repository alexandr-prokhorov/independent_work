# Создать базовый класс Employer (служащий) с методом print().
# Она должна выводить и информацию о служащем. В случае
# базового класса это может быть строка c надписью This is
# Employer class, опционально можете добавить поля, которые
# бы как-то характеризовали ваш класс (имя, фамилия, возраст) -
# это вам пригодится в задании 8.5.
# Создайте от него три производных класса: President, Manager,
# Worker. Переопределите функцию Print() для вывода
# информации, соответствующей каждому типу служащего


class Employer:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print(self):
        print(f"Это класс служащего. Имя и Фамилия{self.first_name} {self.last_name}, возраст {self.age}")


class President(Employer):
    def print(self):
        print(f"Президент: {self.first_name} {self.last_name}, возраст {self.age}. Руководитель компании Apple.")


class Manager(Employer):
    def print(self):
        print(f"Менеджер: {self.first_name} {self.last_name}, возраст {self.age}. Главный дизайнер в компании Apple.")


class Worker(Employer):
    def print(self):
        print(
            f"Работник: {self.first_name} {self.last_name}, возраст {self.age}. Работает над разработкой нового продукта.")


president = President("Тим", "Кук", "64")
manager = Manager("Джонатан ", "Айв ", "57")
worker = Worker("Иван", "Иванов", "25")

president.print()
manager.print()
worker.print()
