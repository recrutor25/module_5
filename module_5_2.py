#!/home/igor/PycharmProjects/module_5
# -*- coding: utf-8 -*-
# Создаю класс House с атрибутами self.name и self.number_of_floors
class House:
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

# Создаю объект класса House с названием и количеством этажей
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вывод на консоль:
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))