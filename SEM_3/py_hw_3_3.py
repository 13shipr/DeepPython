# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

import random

def backpack(my_dict, max_mass):
    things = []
    for key, value in my_dict.items():
        # value = random.choice(list(my_dict.values()))
        if value <= max_mass:
            things.append(key)
            max_mass -= value
    return things

max_mass = 6000
my_dict = {
        'тушенка': 300,
        'фонарь': 500,
        'аптечка': 200,
        'котелок': 200,
        'карабин': 100,
        'лопата': 1000,
        'телевизор': 4000,
        'ноутбук': 3000,
        'радиоприеник': 1000,
        }

print(backpack(my_dict, max_mass))
