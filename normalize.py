text = input("Введите текст: ")

normalized = " ".join(text.split())

print("Исходная длина:", len(text))
print("Новая длина:", len(normalized))
print("Нормализованный текст:", normalized)
print("Количество слов:", len(normalized.split()))
