number = input("Введите положительное число: ")
n = number
a = n + n
b = n + n + n

if int(n) < 0:
    print("Число отрицательное")
else:
    _sum = int(a) + int(b) + int(n)
    print("Сумма: ", _sum)
# _sum = int(a) + int(b) + int(n)

# print(a)
# print(b)
