"""
задача 2 HARD необязательная
Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) ,
причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей.
Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно
и только один раз переместился на другое место и выполнить это за m*n / 2 итераций.
То есть если массив три на четыре, то надо выполнить не более 6 итераций.
И далее в конце опять вывести на экран как таблицу.
"""

from random import randint, choice

while True:
    rows = clmns = 0
    while True:
        while True:
            try:
                rows, clmns = list(map(int, input('Введите количество строк и столбцов: ').split()))
                break
            except ValueError:
                print('Ошибка ввода!')

        if rows * clmns % 2 == 0:
            break
        print('Количество элементов должно быть четным!')

    arr_list = [[randint(1, 10) for _ in range(clmns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(clmns):
            print(arr_list[i][j], end='\t')
        print()

    tuple_list = []
    for i in range(rows):
        for j in range(clmns):
            tuple_list.append((i, j,))

    length = len(tuple_list)
    count_it = 0
    while length > 0:
        ran_elem_1 = choice(tuple_list)
        tuple_list.remove(ran_elem_1)
        ran_elem_2 = choice(tuple_list)
        tuple_list.remove(ran_elem_2)
        length -= 2
        count_it += 1
        arr_list[ran_elem_1[0]][ran_elem_1[1]], arr_list[ran_elem_2[0]][ran_elem_2[1]] = arr_list[ran_elem_2[0]][ran_elem_2[1]], arr_list[ran_elem_1[0]][ran_elem_1[1]]
        print(f'Итерация {count_it}:')
        print(f'Элементы: {ran_elem_1} <-> {ran_elem_2}, {arr_list[ran_elem_1[0]][ran_elem_1[1]]} <-> {arr_list[ran_elem_2[0]][ran_elem_2[1]]}')

    for i in range(rows):
        for j in range(clmns):
            print(arr_list[i][j], end='\t')
        print()