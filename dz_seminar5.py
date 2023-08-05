#  Заполните массив элементами арифметической прогрессии. Её первый элемент,
#  разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
#  an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def a_progression() -> []:
    array = []
    a1 = int(input('введите первый элемент арифметической прогрессии'))
    d = int(input('введите разность'))
    n = int(input('введите количество элементов арифметической прогрессии'))
    for i in range(1, n+1):
        array.append(a1 + d * (i - 1))
    return array

print(a_progression())

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно
#
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

# from random import randint
# def range_index() -> []:
#     array1 = [randint(1, 10)for i in range(20)]
# print("Заданный массив:", array1, sep='\n') торможу((((
#     min = 3
#     max = 18
#     element = 0
#     index = []
#
#
# print(range_index()
def range_index(arr, min_value, max_value) -> list[int]:
    indexes = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indexes.append(i)
    return indexes

arr = [1, 5, 88, 100, 2, -4]
min_value = 33
max_value = 200
result = range_index(arr, min_value, max_value)

print(result)

