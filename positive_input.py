rejected = 0

number = int(input("Введите положительное число: "))

while number <= 0:
    rejected += 1
    number = int(input("Попробуйте снова. Введите положительное число: "))

print("Квадрат числа:", number ** 2)
print("Количество отклонённых попыток:", rejected)
