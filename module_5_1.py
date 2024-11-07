#!/home/igor/PycharmProjects/module_5
# -*- coding: utf-8 -*-

# Создаю класс House с атрибутами self.name и self.number_of_floors
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.num_floors = number_of_floors

 # Создаю метод go_to с параметром new_floor и логикой внутри
    def go_to(self, new_floor: int):

        if 1 <= new_floor < self.num_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует!')

# Создаю объект класса House с названием и количеством этажей
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вывод на консоль:
h1.go_to(5)
h2.go_to(10)
