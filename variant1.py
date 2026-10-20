resource = int(input("Введите уровень игрового ресурса: "))

if resource < 0 or resource > 100:
    print("Ошибка диапазона")
elif resource <= 14:
    print("Пополнить")
elif resource <= 59:
    print("Достаточно")
else:
    print("Большой запас")
