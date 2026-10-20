surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст: "))
subject = input("Любимый предмет: ")
hours = float(input("Часов подготовки в неделю: "))

full_name = name + " " + surname
age_in_4_years = age + 4
hours_4_weeks = hours * 4
hours_per_day = hours / 7

print("=== Карточка студента ===")
print("Полное имя:", full_name)
print("Группа:", group)
print("Город:", city)
print("Возраст:", age)
print("Возраст через 4 года:", age_in_4_years)
print("Любимый предмет:", subject)
print(f"Подготовка за 4 недели: {hours_4_weeks:.2f} ч")
print(f"В среднем в день: {hours_per_day:.2f} ч")
