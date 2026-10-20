# Ожидание А: сумма 5, а не строка "23" (строки склеились)
first = "2"
second = "3"
print("А: типы до:", type(first), type(second))
print("А: до исправления:", first + second)
first = int(first)
second = int(second)
print("А: типы после:", type(first), type(second))
print("А: сумма:", first + second)

# Ожидание Б: возраст через год = 18 (input даёт строку, а не число)
age = input("Возраст: ")
print("Б: тип до:", type(age))
age = int(age)
print("Б: тип после:", type(age))
print("Б: возраст через год:", age + 1)

# Ожидание В: среднее = 7.0 (деление выполняется раньше сложения)
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("В: среднее:", average)
