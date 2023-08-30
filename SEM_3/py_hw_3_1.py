# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.


def rem_duplicates(my_list):
    return list(set([x for x in my_list if my_list.count(x) > 1]))

my_list = [2, 2, 2, 4, 4, 5, 6, 6, 7, 7, 7, 1]

print(rem_duplicates(my_list))



