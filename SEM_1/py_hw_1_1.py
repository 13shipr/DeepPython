a = int(input('enter side a: '))
b = int(input('enter side b: '))
c = int(input('enter side c: '))

def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'такого треугольника нет'
    
    if a != b and b != c and a != c:
        return 'треугольник разносторонний'
    elif a == b and b == c:
        return 'треугольник равносторонний'
    else:
        return 'треугольник равнобедренный'

print(triangle(a, b, c))