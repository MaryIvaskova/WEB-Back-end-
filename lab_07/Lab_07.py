from collections import deque

def evolve_stones(stones, blinks, max_size=10**6):
    """
    Виконує зміни каменів протягом вказаної кількості моргань.
    
    :param stones: Початковий список каменів
    :param blinks: Кількість моргань
    :param max_size: Максимальна кількість каменів для зупинки
    :return: Кількість каменів після заданої кількості моргань
    """
    stones = deque(stones)  # Використовуємо двосторонню чергу для ефективності
    
    for _ in range(blinks):
        new_stones = deque()
        while stones:
            stone = stones.popleft()  # Беремо перший камінь

            if stone == 0:
                new_stones.append(1)  # 0 → 1
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left, right = int(str(stone)[:mid]), int(str(stone)[mid:])
                new_stones.append(left)
                new_stones.append(right)  # Ділимо число
            else:
                new_stones.append(min(stone * 2024, 10**12))  # Обмежуємо ріст

        stones = new_stones  # Оновлюємо список

        # Якщо кількість каменів занадто велика – припиняємо обчислення
        if len(stones) > max_size:
            print(f"⚠️ Досягнуто межу {max_size} каменів! Зупинка.")
            return len(stones)

    return len(stones)  # Повертаємо кількість каменів


# --- Основна програма ---
initial_stones = [2701, 64945, 0, 9959979, 93, 781524, 620, 1]  # Початкові камені

# Обчислюємо кількість каменів після 25 і 75 моргань
stones_after_25 = evolve_stones(initial_stones, 25)
stones_after_75 = evolve_stones(initial_stones, 75)

# Виводимо результати
print(f"- Кількість каменів після 25 моргань: {stones_after_25}")
print(f"- Кількість каменів після 75 моргань: {stones_after_75}")

#Досягнуто межу 1000000 каменів! Зупинка.
#- Кількість каменів після 25 моргань: 186721
#- Кількість каменів після 75 моргань: 1503889