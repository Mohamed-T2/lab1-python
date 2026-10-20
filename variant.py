order = input("Название заказа: ")
customer = input("Имя заказчика: ")

name1 = input("Название первой позиции: ")
qty1 = int(input("Количество: "))
price1 = float(input("Цена единицы (руб.): "))

name2 = input("Название второй позиции: ")
qty2 = int(input("Количество: "))
price2 = float(input("Цена единицы (руб.): "))

delivery = float(input("Стоимость доставки (руб.): "))
paid = float(input("Внесённая сумма (руб.): "))

cost1 = qty1 * price1
cost2 = qty2 * price2
goods = cost1 + cost2
total = goods + delivery
total_qty = qty1 + qty2
change = paid - total

print("=== Заказ:", order, "===")
print("Заказчик:", customer)
print(name1, "|", qty1, "|", f"{price1:.2f}", "|", f"{cost1:.2f}")
print(name2, "|", qty2, "|", f"{price2:.2f}", "|", f"{cost2:.2f}")
print(f"Товары без доставки: {goods:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Всего с доставкой: {total:.2f} руб.")
print("Всего единиц:", total_qty)
print(f"Сдача: {change:.2f} руб.")
