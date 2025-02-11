def is_safe_report(report):

    # Перевіряємо на монотонність (зростаючий або спадаючий порядок)
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    if not (is_increasing or is_decreasing):
        return False

    # Перевіряємо різницю між сусідніми рівнями
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False

    return True


def analyze_reports(file_path):
    """
    Аналізує звіти у файлі та визначає кількість безпечних рядків.
    """
    safe_count = 0

    # Відкриваємо файл через open
    file = open(file_path, 'r')
    for line in file:
        # Преобразуємо рядок у список чисел
        report = list(map(int, line.strip().split()))

        # Перевіряємо, чи рядок є "безпечним"
        if is_safe_report(report):
            safe_count += 1
    file.close()  # Закриваємо файл
    return safe_count


if __name__ == "__main__":
    input_file = "./WEB-Back-end-/Lab_2.2/input_2.txt"  # Шлях до файлу

    try:
        safe_reports = analyze_reports(input_file)
        print(f"Кількість безпечних звітів: {safe_reports}")
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")