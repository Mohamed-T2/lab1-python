first_room = input("Название первой аудитории: ")
second_room = input("Название второй аудитории: ")
print("До обмена:", first_room, second_room)
temp = first_room
first_room = second_room
second_room = temp
print("После обмена:", first_room, second_room)
