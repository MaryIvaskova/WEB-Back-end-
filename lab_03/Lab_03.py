import re  # Імпортуємо модуль для роботи з регулярними виразами

# Визначаємо відповідність слів цифрам
WORD_TO_DIGIT = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def extract_digits(line):
    """
    Основне завдання: знаходить першу і останню цифру у рядку.

    :param line: один рядок з файлу
    :return: двозначне число (перша + остання цифра)
    """
    digits = [char for char in line if char.isdigit()]  # Витягуємо всі цифри з рядка
    
    if digits:  # Якщо знайшли хоча б одну цифру
        return int(digits[0] + digits[-1])  # Комбінуємо першу і останню цифру
    
    return 0  # Якщо цифр немає, повертаємо 0


def extract_spelled_digits(line):
    """
    EXTRA TASK: знаходить першу і останню цифру, враховуючи числа, записані словами.

    :param line: один рядок з файлу
    :return: двозначне число (перша + остання цифра)
    """
    # Регулярний вираз для пошуку як цифр, так і чисел-словами
    pattern = r"one|two|three|four|five|six|seven|eight|nine|\d"
    matches = re.findall(pattern, line)  # Знаходимо всі входження

    if matches:  # Якщо знайшли хоча б одне число
        first = WORD_TO_DIGIT.get(matches[0], matches[0])  # Перетворюємо слово на цифру, якщо треба
        last = WORD_TO_DIGIT.get(matches[-1], matches[-1])
        return int(first + last)  # Комбінуємо першу і останню цифру
    
    return 0  # Якщо нічого не знайдено, повертаємо 0


def calculate_calibration_sum(file_path):
    """
    Читає файл через open() та обчислює суму всіх калібрувальних значень.

    :param file_path: шлях до файлу
    :return: (сума для основного завдання, сума для EXTRA TASK)
    """
    total_sum = 0  # Сума для основного завдання
    total_sum_extra = 0  # Сума для EXTRA TASK

    try:
        file = open(file_path, 'r')  # Відкриваємо файл
        for line in file:
            total_sum += extract_digits(line)  # Додаємо число з основного завдання
            total_sum_extra += extract_spelled_digits(line)  # Додаємо число з EXTRA TASK

        file.close()  # Закриваємо файл після зчитування
        return total_sum, total_sum_extra  # Повертаємо обидва значення

    except FileNotFoundError:
        print(f"⚠️ Файл не знайдено: {file_path}")
        return None, None  # Якщо файл не знайдено


# --- Основна програма ---
file_path = "./WEB-Back-end-/lab_03/input.txt"  # Шлях до файлу

# Обчислюємо суму калібрувальних значень
sum_main, sum_extra = calculate_calibration_sum(file_path)

# Виводимо результат
if sum_main is not None:
    print(f" Сума калібрувальних значень (основне завдання): {sum_main}")
    print(f" - EXTRA Сума калібрувальних значень : {sum_extra}")

# Сума калібрувальних значень (основне завдання): 55538
# EXTRA Сума калібрувальних значень : 54868