a = int(input("Введите a: "))
b = int(input("Введите b: "))

if a <= b:
    for number in range(a, b + 1):
        print(number)
else:
    for number in range(a, b - 1, -1):
        print(number)
