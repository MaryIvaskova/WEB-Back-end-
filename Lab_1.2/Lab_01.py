from collections import Counter  # Імпортуємо Counter для підрахунку кількості входжень елементів

def calculate_distance(left_list, right_list):
    """
    Обчислює загальну відстань між числами у двох списках після сортування.

    :param left_list: список чисел зліва
    :param right_list: список чисел справа
    :return: загальна сума відстаней між відповідними парами
    """
    left_sorted = sorted(left_list)  # Сортуємо лівий список
    right_sorted = sorted(right_list)  # Сортуємо правий список

    # Обчислюємо відстань між відповідними парами чисел
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    
    return total_distance


def calculate_similarity_score(left_list, right_list):
    """
    Обчислює коефіцієнт схожості між двома списками.
    
    :param left_list: список чисел зліва
    :param right_list: список чисел справа
    :return: загальний коефіцієнт схожості
    """
    right_count = Counter(right_list)  # Підраховуємо, скільки разів кожне число зустрічається у правому списку
    similarity_score = sum(num * right_count[num] for num in left_list)  # Обчислюємо загальну суму

    return similarity_score


# --- Основна програма ---
if __name__ == "__main__":
    # Зчитуємо списки з файлу
    file_path = "./WEB-Back-end-/Lab_1.2/input_1.txt"  # Файл із числами

    left_list = []
    right_list = []

    # Відкриваємо файл для читання
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())  # Розділяємо числа в рядку
            left_list.append(left)  # Додаємо у лівий список
            right_list.append(right)  # Додаємо у правий список

    # --- Основне завдання ---
    total_distance = calculate_distance(left_list, right_list)
    print(f"✅ Загальна сума відстаней: {total_distance}")

    # --- EXTRA TASK (Коефіцієнт схожості) ---
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"🎯 Коефіцієнт схожості: {similarity_score}")