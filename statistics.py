n = int(input("Введите количество чисел: "))

total = 0
positive_count = 0

for i in range(n):
    number = int(input("Введите целое число: "))

    total += number

    if number > 0:
        positive_count += 1

    if i == 0:
        maximum = number
    elif number > maximum:
        maximum = number

print("Сумма:", total)
print("Количество положительных чисел:", positive_count)
print("Максимум:", maximum)
