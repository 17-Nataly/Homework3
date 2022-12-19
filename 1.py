"""Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12"""


def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = [2, 3, 5, 9, 3]
sum_odd_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)