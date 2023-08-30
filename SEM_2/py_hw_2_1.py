# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def my_fractions(frac_1, frac_2):
    num_1, denom_1 = map(int, frac_1.split('/'))
    num_2, denom_2 = map(int, frac_2.split('/'))
    sum_frac_num = num_1 * denom_2 + num_2 * denom_1
    sum_frac_denom = denom_1 * denom_2
    sum_frac = (sum_frac_num, sum_frac_denom)
    prod_frac_num = num_1 * num_2
    prod_frac_denom = denom_1 * denom_2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac

frac_1 = '2/7'
frac_2 = '4/6'
sum_frac, prod_frac = my_fractions(frac_1, frac_2)

print(f'Сумма несокращенных дробей -> {frac_1} и {frac_2} - {sum_frac[0]}/{sum_frac[1]}')
print(f'Произведение несокращенных дробей -> {frac_1} и {frac_2} - {prod_frac[0]}/{prod_frac[1]}\n')
print(f'Проверка суммы через модуль Fraction -> {Fraction(frac_1) + Fraction(frac_2)}')
print(f'Проверка произведения через модуль Fraction -> {Fraction(frac_1) * Fraction(frac_2)}')