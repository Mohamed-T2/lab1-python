numbers = []

for part in input("Entrez des nombres entiers : ").split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []

    for index, number in enumerate(numbers):
        if number == maximum:
            positions.append(index)

    print(f"Максимум: {maximum}")
    print(f"Индексы: {positions}")
