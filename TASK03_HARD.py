"""
Задача HARD SORT необязательная.
Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
Отсортировать элементы по возрастанию слева направо и сверху вниз.

Например, задан массив:
1 4 7 2
5 9 10 3

После сортировки
1 2 3 4
5 7 9 10
"""
from random import randint
while True:
    while True:
        try:
            rows, clmns = list(map(int, input('Введите количество строк и столбцов: ').split()))
            break
        except ValueError:
            print('Ошибка ввода!')

    arr_list = [[randint(1, 10) for _ in range(clmns)] for _ in range(rows)]
    print(arr_list)

    sort_list = []

    for _ in arr_list:
        sort_list.extend(_)

    sort_list = sorted(sort_list)

    k = 0
    for i in range(rows):
        for j in range(clmns):
            arr_list[i][j] = sort_list[k]
            k += 1


    print(arr_list)

