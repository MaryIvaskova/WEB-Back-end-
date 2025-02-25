import re  # Імпортуємо модуль для роботи з регулярними виразами

def read_input(file_path):
    """
    Зчитує список звітів із файлу.

    :param file_path: шлях до файлу
    :return: список списків чисел (рівнів)
    """
    reports = []
    
    try:
        with open(file_path, "r") as file:
            for line in file:
                numbers = list(map(int, re.findall(r"-?\d+", line)))  # Витягуємо всі числа
                if numbers:  # Додаємо лише непорожні рядки
                    reports.append(numbers)
        return reports

    except FileNotFoundError:
        print(f"⚠️ Файл не знайдено: {file_path}")
        return None


def is_safe(report):
    """
    Перевіряє, чи звіт безпечний.

    Умови:
    1. Всі рівні або зростають, або спадають.
    2. Різниця між сусідніми рівнями повинна бути від 1 до 3 включно.

    :param report: список чисел (рівнів)
    :return: True, якщо звіт безпечний, False - якщо ні
    """
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    if not (increasing or decreasing):  # Якщо не зростає і не спадає - не безпечний
        return False

    return all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))


def can_become_safe(report):
    """
    EXTRA TASK: Перевіряє, чи можна зробити звіт безпечним видаленням одного рівня.

    :param report: список чисел (рівнів)
    :return: True, якщо після видалення одного рівня звіт стає безпечним, False - якщо ні
    """
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]  # Видаляємо один рівень
        if is_safe(new_report):  # Перевіряємо, чи став звіт безпечним
            return True
    return False


def count_safe_reports(file_path):
    """
    Читає файл через open() та підраховує кількість безпечних звітів.

    :param file_path: шлях до файлу
    :return: (кількість безпечних звітів, кількість "виправлених" звітів)
    """
    reports = read_input(file_path)
    if reports is None:
        return None, None

    safe_count = 0  # Лічильник безпечних звітів
    improved_safe_count = 0  # Лічильник виправлених звітів

    for report in reports:
        if is_safe(report):
            safe_count += 1  # Додаємо, якщо звіт безпечний
        elif can_become_safe(report):
            improved_safe_count += 1  # Додаємо, якщо можна зробити безпечним

    return safe_count, safe_count + improved_safe_count


# --- Основна програма ---
if __name__ == "__main__":
    file_path = "./WEB-Back-end-/lab_02/input.txt"  # Шлях до файлу

    # Підраховуємо кількість безпечних звітів
    safe_reports, improved_safe_reports = count_safe_reports(file_path)

    if safe_reports is not None:
        print(f"Кількість безпечних звітів: {safe_reports}")
        print(f"Extra - Кількість звітів, які стали безпечними після виправлення: {improved_safe_reports}")

#Кількість безпечних звітів: 218
# Extra - Кількість звітів, які стали безпечними після виправлення: 290