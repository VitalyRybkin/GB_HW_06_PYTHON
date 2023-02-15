"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]

"""
from random import randint

size = int(input('Введите размер списка: '))

while True:
    try:
        min_elem, max_elem = list(map(int, input('Введите диапазон через пробел: ').split()))
        break
    except ValueError:
        print('Ошибка ввода!')

if min_elem > max_elem:
    min_elem, max_elem = max_elem, min_elem

num_list = [randint(-10, 10) for i in range(size)]
res = []

for k,v in enumerate(num_list):
    if v > min_elem and v < max_elem:
        res.append(k)


print('Список: ', num_list)
print('Результат: ', res)
