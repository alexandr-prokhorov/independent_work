# Для классов из задания 8.4 реализуйте магический метод str, а
# также метод int (должен возвращать возраст служащего).

class Employer:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"Служащий: {self.first_name} {self.last_name}, Возраст {self.age}"

    def __int__(self):
        return self.age

    def print(self):
        print(f"Это класс служащего. Имя и Фамилия{self.first_name} {self.last_name}, возраст {self.age}")


class President(Employer):
    def __str__(self):
        return f"Президент: {self.first_name} {self.last_name}, Возраст {self.age}"

    def print(self):
        print(f"Президент: {self.first_name} {self.last_name}, возраст {self.age}. Руководитель компании Apple.")


class Manager(Employer):
    def __str__(self):
        return f"Менеджер: {self.first_name} {self.last_name}, возраст {self.age}."

    def print(self):
        print(f"Менеджер: {self.first_name} {self.last_name}, возраст {self.age}. Главный дизайнер в компании Apple.")


class Worker(Employer):
    def __str__(self):
        return f"Работник: {self.first_name} {self.last_name}, возраст {self.age}."

    def print(self):
        print(
            f"Работник: {self.first_name} {self.last_name}, возраст {self.age}. Работает над разработкой продукта.")


president = President("Тим", "Кук", 64)
manager = Manager("Джонатан ", "Айв ", 57)
worker = Worker("Иван", "Иванов", 25)
print()
president.print()
manager.print()
worker.print()
print()
print(str(president))
print(str(manager))
print(str(worker))
print()
print(f"Возраст: {int(president)}")
print(f"Возраст: {int(manager)}")
print(f"Возраст: {int(worker)}")
