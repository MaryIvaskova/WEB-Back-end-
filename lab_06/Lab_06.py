# Визначаємо значення фігур
SHAPE_SCORE = {"X": 1, "Y": 2, "Z": 3}  # Твої ходи: X (Rock), Y (Paper), Z (Scissors)
OUTCOME_SCORE = {
    ("A", "X"): 3, ("A", "Y"): 6, ("A", "Z"): 0,  # Rock vs (Rock, Paper, Scissors)
    ("B", "X"): 0, ("B", "Y"): 3, ("B", "Z"): 6,  # Paper vs (Rock, Paper, Scissors)
    ("C", "X"): 6, ("C", "Y"): 0, ("C", "Z"): 3   # Scissors vs (Rock, Paper, Scissors)
}

def calculate_total_score(file_path):
    """
    Обчислює загальну кількість очок відповідно до стратегії.

    :param file_path: Шлях до файлу зі стратегією гри
    :return: Загальна кількість очок
    """
    total_score = 0

    try:
        with open(file_path, "r") as file:  # Відкриваємо файл
            for line in file:
                parts = line.strip().split()
                if len(parts) != 2:
                    continue  # Пропускаємо некоректні рядки

                opponent, my_choice = parts  # Витягуємо дані
                round_score = SHAPE_SCORE[my_choice] + OUTCOME_SCORE[(opponent, my_choice)]
                total_score += round_score  # Додаємо очки за цей раунд

        return total_score

    except FileNotFoundError:
        print(f"⚠️ Файл не знайдено: {file_path}")
        return None


# --- Основна програма ---
if __name__ == "__main__":
    file_path = "./WEB-Back-end-/lab_06/input.txt"  # Шлях до файлу

    # Обчислюємо загальну кількість очок
    total_score = calculate_total_score(file_path)

    # Виводимо результат
    if total_score is not None:
        print(f"Загальна кількість очок: {total_score}")

#Загальна кількість очок: 8933