n = int(input("Введите количество чисел: "))

count = 0
total = 0

for i in range(n):
    number = int(input("Введите целое число: "))

    if number != 0:
        count += 1
        total += number

print("Количество ненулевых чисел:", count)
print("Сумма ненулевых чисел:", total)
