"""Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове."""

string_input = input("Введите слова в строку: ").split()

for index, el in enumerate(string_input, 1):
    # Выводим слова полностью, если len(el) <= 10, иначе el обрезаем до 10 символов и выводим результат.
    print(index, el) if len(el) <= 10 else print(index, (el[:10]))
