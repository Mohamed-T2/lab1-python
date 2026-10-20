subject1 = input("Название первого предмета: ")
subject2 = input("Название второго предмета: ")
count1 = int(input("Занятий в неделю по первому предмету: "))
count2 = int(input("Занятий в неделю по второму предмету: "))
duration1 = int(input("Длительность одного занятия по первому (мин): "))
duration2 = int(input("Длительность одного занятия по второму (мин): "))
available_hours = float(input("Доступное время в неделю (часы): "))

minutes1 = count1 * duration1
minutes2 = count2 * duration2
total_minutes = minutes1 + minutes2
total_hours = total_minutes / 60
free_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4

print(subject1, "- минут:", minutes1)
print(subject2, "- минут:", minutes2)
print("Всего минут:", total_minutes)
print(f"Всего часов: {total_hours:.2f}")
print(f"Свободно часов: {free_hours:.2f}")
print(f"За четыре недели: {four_weeks_hours:.2f} ч")
