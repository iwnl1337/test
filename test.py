import json
import os

FILENAME = "qa_result.json"

# Загружаем существующие данные, если файл есть
if os.path.exists(FILENAME):
    with open(FILENAME, "r", encoding="utf-8") as f:
        try:
            qa_pairs = json.load(f)
        except json.JSONDecodeError:
            qa_pairs = []
else:
    qa_pairs = []

print("Вводи вопросы и ответы. Чтобы завершить — оставь вопрос пустым и нажми Enter.\n")

while True:
    question = input("Вопрос: ").strip()
    if not question:
        print("Завершено. Все данные сохранены в", FILENAME)
        break

    answer = input("Ответ: ").strip()
    qa_pairs.append({"question": question, "answer": answer})

    # Сохраняем после каждого ввода
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(qa_pairs, f, ensure_ascii=False, indent=2)

    print("Добавлено! Можно вводить следующий вопрос.\n")
