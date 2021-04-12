"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""

list_static = [7, 5, 3, 3, 2, 1]
# Преобразуем в кортеж для экономии памяти.
list_static_2 = tuple(list_static)

number_input = int(input("Введите целое число в качестве элемента рейтинга: "))
index = 0

for i in list_static:
    if number_input <= i:
        index += 1
# Вставляем введённое число следующим за найденным индексом, либо следующим по убыванию.
list_static.insert(index, number_input)

print(f"Исходный список: {list_static_2}\nРезультат: {list_static}")
