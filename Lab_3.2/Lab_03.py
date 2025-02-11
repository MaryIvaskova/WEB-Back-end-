import re

def extract_calibration_value(line):
    """
    Витягує калібрувальне значення з рядка.
    """
    # Знаходимо всі цифри у рядку
    digits = re.findall(r'\d', line)
    if len(digits) >= 2:
        # Формуємо двоцифрове число з першої та останньої цифри
        return int(digits[0] + digits[-1])
    return 0  # Якщо цифр менше двох, повертаємо 0

def calculate_total_calibration(file_path):
    """
    Обчислює суму калібрувальних значень для всіх рядків у файлі.
    """
    total_calibration = 0

    # Відкриваємо файл через open
    file = open(file_path, 'r')
    for line in file:
        # Обчислюємо калібрувальне значення для кожного рядка
        calibration_value = extract_calibration_value(line.strip())
        total_calibration += calibration_value
    file.close()  # Закриваємо файл
    return total_calibration


if __name__ == "__main__":
    input_file = "./WEB-Back-end-/Lab_3.2/input_3.txt"  # Шлях до файлу

    try:
        total = calculate_total_calibration(input_file)
        print(f"Загальна сума калібрувальних значень: {total}")
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")