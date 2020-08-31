num_init = int(input("Введите положительное число: "))
greatest_dig = num_init % 10
num = num_init

while num > 0:
    digit = num % 10
    if digit > greatest_dig:
        greatest_dig = digit
        if greatest_dig == 9:
            break
    num = num // 10
print("Самая большая цифра: ", greatest_dig)
