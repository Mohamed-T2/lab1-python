numbers = []

for part in input("Entrez des nombres entiers : ").split():
    numbers.append(int(part))

selected = []

for number in numbers:
    if number != 0:
        selected.append(number)

sorted_numbers = sorted(selected)

print(f"Исходный список: {numbers}")
print(f"Выбранные числа: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted_numbers}")
