#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль

# уберите слона
#  и выведите список на консоль

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
def zoo_shaffles():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
    birds = ['rooster', 'ostrich', 'lark', ]
    zoo.insert(1, 'bear')
    print(zoo)
    zoo += birds
    print(zoo)
    zoo.remove('elephant')
    print(zoo)
    print(f"Номер клетки льва: {zoo.index('lion') + 1}, Номер клетки жаворонка: {zoo.index('lark') + 1}")
    return 

zoo_shaffles()
