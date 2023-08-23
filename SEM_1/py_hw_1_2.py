def prime_number():
    num = int(input('введите целое число: '))
    if 0 > num >= 100000:
        return 'введите число от 0 до 100000'
    if num == 1 or num == 0:
        return 'число не является простым'
    for _ in range(2, int(num**0.5) + 1):
        if num % _ == 0:
            return 'число составное'
    return 'число простое'

print(prime_number())