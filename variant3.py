text = input("Введите текст: ")

words = text.split()
matches = []

for word in words:
    cleaned = word.strip(".,!?;:").lower()

    if cleaned == "":
        continue

    if "а" not in cleaned:
        matches.append(cleaned)
        print(cleaned)

print("Количество:", len(matches))

if len(matches) == 0:
    print("Нет совпадений")
