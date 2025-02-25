import re  # Імпортуємо модуль для роботи з регулярними виразами

# Обмеження на кількість кубиків у мішку
BAG_LIMITS = {"red": 12, "green": 13, "blue": 14}

def parse_game_data(line):
    """
    Парсить рядок гри та повертає ID гри та список раундів.

    :param line: Рядок формату "Game X: N color, M color; ..."
    :return: ID гри, список раундів (список словників {color: count})
    """
    match = re.match(r"Game (\d+): (.+)", line.strip())
    if not match:
        return None, []

    game_id = int(match.group(1))  # Отримуємо ID гри
    rounds = match.group(2).split("; ")  # Розбиваємо на окремі раунди

    game_rounds = []
    for round_data in rounds:
        round_info = {}
        for cube in round_data.split(", "):  # Обробляємо кожен колір
            count, color = cube.split(" ")
            round_info[color] = int(count)
        game_rounds.append(round_info)

    return game_id, game_rounds


def is_game_possible(game_rounds):
    """
    Перевіряє, чи гра можлива, враховуючи обмеження на кубики.

    :param game_rounds: Список словників {color: count} для кожного раунду гри
    :return: True, якщо гра можлива, інакше False
    """
    for round_info in game_rounds:
        for color, count in round_info.items():
            if count > BAG_LIMITS[color]:  # Перевіряємо обмеження
                return False
    return True


def calculate_minimum_cubes(game_rounds):
    """
    Знаходить мінімальний набір кубиків, необхідний для гри.

    :param game_rounds: Список словників {color: count} для кожного раунду гри
    :return: Словник з мінімальною кількістю кожного кольору
    """
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    
    for round_info in game_rounds:
        for color, count in round_info.items():
            min_cubes[color] = max(min_cubes[color], count)  # Беремо максимальну потребу

    return min_cubes


def game_power(min_cubes):
    """
    Обчислює потужність мінімального набору кубиків (добуток).

    :param min_cubes: Словник {color: count}
    :return: Числове значення потужності
    """
    return min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]


def process_games(file_path):
    """
    Обробляє всі ігри у файлі та повертає суму ID можливих ігор та суму потужностей.

    :param file_path: Шлях до файлу з іграми
    :return: (Сума ID можливих ігор, Сума потужностей мінімальних наборів)
    """
    total_possible_ids = 0  # Сума ID можливих ігор
    total_power_sum = 0  # Сума потужностей мінімальних наборів

    try:
        with open(file_path, "r") as file:  # Відкриваємо файл
            for line in file:
                game_id, game_rounds = parse_game_data(line)

                if game_id is None:
                    continue  # Пропускаємо рядки, які не відповідають формату

                # Основне завдання
                if is_game_possible(game_rounds):
                    total_possible_ids += game_id  # Додаємо ID можливої гри

                # EXTRA TASK
                min_cubes = calculate_minimum_cubes(game_rounds)
                total_power_sum += game_power(min_cubes)  # Додаємо потужність

        return total_possible_ids, total_power_sum

    except FileNotFoundError:
        print(f"⚠️ Файл не знайдено: {file_path}")
        return None, None


# --- Основна програма ---
if __name__ == "__main__":
    file_path = "./WEB-Back-end-/lab_05/input.txt"  # Шлях до файлу

    # Обчислюємо результати
    sum_possible_ids, sum_power_sets = process_games(file_path)

    # Виводимо результати
    if sum_possible_ids is not None:
        print(f"Сума ID можливих ігор: {sum_possible_ids}")
        print(f"Extra - Сума потужностей мінімальних наборів: {sum_power_sets}")

#Сума ID можливих ігор: 2810
#Extra - Сума потужностей мінімальних наборів: 69110