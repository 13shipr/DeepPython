# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
import random

MAX_MASS = 6000

def bagage():
    sum_value = 0
    print(f'эти вещи вошли в рюкзак: \n')
    for key, value in my_dict.items():
        value = random.sample(list(my_dict.values()), k=9)
        sum_value += value
        if sum_value < MAX_MASS:
            # value = random.sample(list(my_dict.values()), k=9)
        # sum_value += value
        # print(sum_value, key, value)
        # if sum_value < MAX_MASS:
            print(f'{key} весом {value} грамм')

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

bagage()


# print(f'все эти вещи вошли в рюкзак: {bagage}')
