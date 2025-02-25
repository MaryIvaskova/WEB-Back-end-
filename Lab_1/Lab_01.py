import re  # Імпортуємо модуль для роботи з регулярними виразами
from collections import Counter  # Для підрахунку частоти елементів у списках

def read_input(file_path):
    """
    Зчитує числа з файлу у вигляді двох списків.

    :param file_path: шлях до файлу
    :return: два списки (left_list, right_list)
    """
    left_list = []
    right_list = []
    
    try:
        with open(file_path, "r") as file:
            for line in file:
                numbers = re.findall(r"\d+", line)  # Витягуємо всі числа з рядка
                if len(numbers) == 2:  # Має бути рівно два числа в рядку
                    left_list.append(int(numbers[0]))
                    right_list.append(int(numbers[1]))
        return left_list, right_list

    except FileNotFoundError:
        print(f"⚠️ Файл не знайдено: {file_path}")
        return None, None


def calculate_distance(left_list, right_list):
    """
    Обчислює загальну відстань між числами у двох списках після сортування.

    :param left_list: список чисел зліва
    :param right_list: список чисел справа
    :return: загальна сума відстаней між відповідними парами
    """
    left_sorted = sorted(left_list)  # Сортуємо лівий список
    right_sorted = sorted(right_list)  # Сортуємо правий список

    # Обчислюємо абсолютну різницю між відповідними парами чисел
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    
    return total_distance  # Повертаємо загальну суму відстаней


def calculate_similarity_score(left_list, right_list):
    """
    Обчислює коефіцієнт схожості між двома списками.

    :param left_list: список чисел зліва
    :param right_list: список чисел справа
    :return: загальний коефіцієнт схожості
    """
    right_count = Counter(right_list)  # Підраховуємо, скільки разів кожне число зустрічається у правому списку
    similarity_score = sum(num * right_count[num] for num in left_list)  # Кожен елемент множимо на кількість його входжень
    
    return similarity_score  # Повертаємо загальний коефіцієнт схожості


# --- Основна програма ---
if __name__ == "__main__":
    file_path = "./WEB-Back-end-/Lab_1/input.txt"  # Шлях до файлу

    # Зчитуємо списки з файлу
    left_list, right_list = read_input(file_path)

    if left_list is not None and right_list is not None:
        # --- Основне завдання ---
        total_distance = calculate_distance(left_list, right_list)
        print(f"Загальна сума відстаней: {total_distance}")

        # --- EXTRA TASK ---
        similarity_score = calculate_similarity_score(left_list, right_list)
        print(f"Extra - Коефіцієнт схожості: {similarity_score}")