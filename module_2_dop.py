import random


def find_pairs(number):
    """Находит пары чисел (x, y), сумма которых кратна заданному числу."""
    pairs = []
    for x in range(3, number + 1):
        for y in range(3, number + 1):
            if number % (x + y) == 0:
                pairs.append((x, y))
    return pairs


# Симуляция работы системы
while True:
    # Генерируем случайное число для первой вставки (от 3 до 20)
    stone_number = random.randint(3, 20)
    print(f"Число на первой вставке: {stone_number}")

    # Находим пары для этого числа
    pairs = find_pairs(stone_number)

    print(f"Подходящие пары чисел для {stone_number}: {pairs}")

    # Прерываем бесконечный цикл, если решено (вы можете настроить, например, на один проход)
    break
n = random.randint(3, 20)
ans = ""

for i in range (1, n):
    for j in range (i+1, n):
        if n % (i + j) == 0:
            ans += str (i) + str (j)
print("Подходящие пары чисел для:", n, ans)