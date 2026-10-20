def word_counts(text):
    """Подсчитывает количество слов в тексте."""
    punctuation = ".,!?;:"
    counts = {}

    for word in text.lower().split():
        word = word.strip(punctuation)
        if word:
            counts[word] = counts.get(word, 0) + 1

    return counts


def print_word_counts(text):
    """Выводит слова в алфавитном порядке."""
    counts = word_counts(text)

    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    """Возвращает общие темы."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Возвращает все уникальные темы."""
    return sorted(set(first) | set(second))


def totals_by_category(records):
    """Вычисляет сумму баллов по категориям."""
    totals = {}

    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]

    return totals


def titles_in_category(records, category):
    """Возвращает названия заданий выбранной категории."""
    return [
        record["title"]
        for record in records
        if record["category"] == category
    ]


def sorted_category_totals(records):
    """Сортирует категории по сумме и названию."""
    return sorted(
        totals_by_category(records).items(),
        key=lambda item: (-item[1], item[0])
    )


def main():
    records = [
        {"title": "Калькулятор", "category": "основное", "amount": 9},
        {"title": "Список задач", "category": "дополнительное", "amount": 7},
        {"title": "Конвертер", "category": "основное", "amount": 8},
        {"title": "Игра угадай число", "category": "тестирование", "amount": 6},
        {"title": "Работа со строками", "category": "дополнительное", "amount": 5},
    ]

    print("Подсчёт слов:")
    print_word_counts("Python, python! SQL")

    print("\nОбщие темы:")
    print(common_topics(["python", "sql"], ["sql", "git"]))

    print("\nВсе темы:")
    print(all_topics(["python", "sql"], ["sql", "git"]))

    record = {"title": "Python", "hours": 4}
    record["hours"] = 6
    record["completed"] = False

    pair = (record["title"], record["hours"])
    title, hours = pair
    print(f"\nПара: {title}, {hours}")

    print("\nСуммы по категориям:")
    totals = totals_by_category(records)

    for category in sorted(totals):
        print(f"{category}: {totals[category]}")

    category = input("\nВведите категорию: ")
    print("Найденные задания:", titles_in_category(records, category))

    print("\nСортировка по сумме:")
    print(sorted_category_totals(records))


if _name_ == "_main_":
    main()
