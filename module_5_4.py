#!/home/igor/PycharmProjects/module_5
# -*- coding: utf-8 -*-

# Создаю класс House с атрибутами self.name и self.number_of_floors
class House:
    # Создаю список для хранения истории
    houses_history = []

    # Создаю метод для записи здания в историю
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.num_floors = number_of_floors

    # Создаю метод go_to с параметром new_floor и логикой внутри
    # него на основе задачи 5_1.
    def go_to(self, new_floor: int):
        if 1 < new_floor > self.num_floors:
            print('Такого этажа не существует!')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    # Дополняю класс House методом возврата строки: "Название: <название>,
    # кол-во этажей: <этажи>"
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.num_floors}"

# Дополняю класс House методом возврата кол-ва этажей здания
    def __len__(self):
        return self.num_floors

    # Дополняю класс House следующими методами:
    # Метод сравнения на равенства: True, если количество этажей self == other
    def __eq__(self, other):
        if isinstance(other, House):
            return self.num_floors == other.num_floors
        else:
            return False

    # Методом сравнения (количество этажей) "меньше чем"
    def __lt__(self, other):
        if isinstance(other, House):
            return self.num_floors < other.num_floors
        else:
            return NotImplemented

     # Методом сравнения (количество этажей) "меньше или равно"
    def __le__(self, other):
        if isinstance(other, House):
             return self.num_floors <= other.num_floors
        else:
            return NotImplemented

    # Методом сравнения (количество этажей) "больше чем"
    def __gt__(self, other):
        if isinstance(other, House):
            return self.num_floors > other.num_floors
        else:
            return NotImplemented

    # Методом сравнения (количество этажей) "больше или равно"
    def __ge__(self, other):
        if isinstance(other, House):
            return self.num_floors >= other.num_floors
        else:
            return NotImplemented

    # Метод сравнения на неравенство
    def __ne__(self, other):
        if isinstance(other, House):
            return self.num_floors != other.num_floors
        else:
            return True

    # Метод использования оператора сложения
    def __add__(self, value):
        if isinstance(value, int):
            self.num_floors = self.num_floors+ value
            return self
        else:
            return NotImplemented

    # Метод симметричного сложения
    def __radd__(self, value):
        return self.__add__(value)

    # Метод сложения с присваиванием +=
    def __iadd__(self, value):
        return self.__add__(value)

# метод уничтожения класса
    def __del__(self):
        print(self.name, ' снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
#
# Удаление объектов
del h2
del h3
#
print(House.houses_history)

