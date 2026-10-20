numbers = []

for part in input("Entrez des nombres entiers : ").split():
    numbers.append(int(part))

transformed = []

for number in numbers:
    if number < 0:
        transformed.append(abs(number))
    else:
        transformed.append(number)

print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed}")
