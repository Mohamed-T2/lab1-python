price = int(input("Цена одной тетради (руб.): "))
count = int(input("Количество: "))
paid = int(input("Переданная сумма: "))

cost = price * count
change = paid - cost

print(f"Стоимость: {cost}")
print(f"Сдача: {change}")
