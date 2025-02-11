def is_safe(report):
    """
    Перевіряє, чи список чисел є "безпечним".
    
    Умови:
    1. Всі числа повинні бути або зростаючими, або спадними.
    2. Різниця між сусідніми числами повинна бути від 1 до 3 включно.

    :param report: список чисел (один рядок із файлу)
    :return: True, якщо звіт безпечний, False - якщо ні
    """
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))  # Чи всі числа зростають?
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))  # Чи всі числа спадають?

    if not (increasing or decreasing):  # Якщо не зростає і не спадає - не безпечний
        return False

    # Перевіряємо, чи всі різниці між сусідніми числами знаходяться в межах 1-3
    return all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))


def can_become_safe(report):
    """
    EXTRA TASK: Перевіряє, чи можна зробити звіт безпечним видаленням одного рівня.

    :param report: список чисел
    :return: True, якщо видалення 1 рівня робить звіт безпечним, False - якщо ні
    """
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]  # Видаляємо один рівень
        if is_safe(new_report):  # Перевіряємо, чи став звіт безпечним
            return True
    return False


def count_safe_reports(file_path):
    """
    Читає файл через open() та підраховує кількість "безпечних" звітів.

    :param file_path: шлях до файлу
    :return: (кількість безпечних звітів, кількість "виправлених" звітів)
    """
    safe_count = 0  # Лічильник безпечних звітів
    improved_safe_count = 0  # Лічильник виправлених звітів

    try:
        file = open(file_path, 'r')  # Відкриваємо файл через open()
        for line in file:
            numbers = list(map(int, line.split()))  # Перетворюємо рядок у список чисел
            if is_safe(numbers):  # Перевіряємо, чи безпечний звіт
                safe_count += 1  # Збільшуємо лічильник
            elif can_become_safe(numbers):  # Перевіряємо, чи можна зробити безпечним
                improved_safe_count += 1

        file.close()  # Закриваємо файл вручну після зчитування
        return safe_count, safe_count + improved_safe_count  # Повертаємо обидва значення

    except FileNotFoundError:
        print(f"⚠️ Файл не знайдено: {file_path}")
        return None, None  # Якщо файл не знайдено


# --- Основна програма ---
file_path = "./WEB-Back-end-/Lab_2.2/input_2.txt"  # Шлях до файлу

# Підраховуємо кількість безпечних звітів
safe_reports, improved_safe_reports = count_safe_reports(file_path)

# Виводимо результат
if safe_reports is not None:
    print(f" Кількість безпечних звітів: {safe_reports}")
    print(f" Кількість звітів, які стали безпечними після виправлення: {improved_safe_reports}")