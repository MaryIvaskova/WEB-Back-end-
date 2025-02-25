def parse_terminal_output(file_path):
    """
    Парсить вивід терміналу та будує дерево директорій.

    :param file_path: шлях до файлу
    :return: словник, що представляє файлову систему
    """
    fs_tree = {"/": {}}  # Створюємо кореневу директорію
    current_path = []  # Масив для збереження поточного шляху

    try:
        file = open(file_path, "r")  # Відкриваємо файл через open()
        for line in file:
            parts = line.strip().split()

            if parts[0] == "$":  # Команда терміналу
                if parts[1] == "cd":
                    if parts[2] == "/":  # Перехід до кореня
                        current_path = []
                    elif parts[2] == "..":  # Перехід на рівень вище
                        if current_path:
                            current_path.pop()
                    else:  # Перехід до нової директорії
                        current_path.append(parts[2])

            elif parts[0] == "dir":  # Виявлено директорію
                dir_name = parts[1]
                current_dir = get_nested_dir(fs_tree, current_path)
                current_dir[dir_name] = {}

            else:  # Виявлено файл (формат: <розмір> <назва>)
                file_size = int(parts[0])
                file_name = parts[1]
                current_dir = get_nested_dir(fs_tree, current_path)
                current_dir[file_name] = file_size

        file.close()  # Закриваємо файл
        return fs_tree

    except FileNotFoundError:
        print(f"⚠️ Файл не знайдено: {file_path}")
        return None


def get_nested_dir(fs_tree, path):
    """
    Отримує вкладену директорію за шляхом.

    :param fs_tree: дерево файлової системи
    :param path: список директорій, що формує шлях
    :return: вкладений словник (поточна директорія)
    """
    current = fs_tree["/"]
    for directory in path:
        current = current[directory]
    return current


def calculate_directory_sizes(fs_tree, path="/"):
    """
    Рекурсивно обчислює розмір кожної директорії.

    :param fs_tree: дерево файлової системи
    :param path: поточний шлях
    :return: словник {директорія: розмір}
    """
    sizes = {}
    
    def helper(node, full_path):
        total_size = 0
        for name, value in node.items():
            if isinstance(value, dict):  # Це вкладена директорія
                dir_size = helper(value, f"{full_path}/{name}")
                sizes[f"{full_path}/{name}"] = dir_size
                total_size += dir_size
            else:  # Це файл
                total_size += value

        return total_size

    root_size = helper(fs_tree["/"], "/")
    sizes["/"] = root_size  # Додаємо кореневу директорію
    return sizes


# --- Основна програма ---
file_path = "./WEB-Back-end-/Lab_4/input.txt"  # Шлях до файлу

# Парсимо файлову систему
fs_tree = parse_terminal_output(file_path)

if fs_tree:
    # Обчислюємо розміри директорій
    dir_sizes = calculate_directory_sizes(fs_tree)

    # Фільтруємо директорії з розміром ≤ 100000
    filtered_sizes = {k: v for k, v in dir_sizes.items() if v <= 100000}

    # Обчислюємо загальну суму
    total_size = sum(filtered_sizes.values())

    print(f"Сума розмірів директорій ≤ 100000: {total_size}")