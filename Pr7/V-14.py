# 1
def count_divisors(num):
    """Возвращает количество делителей числа."""
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count


def find_numbers_with_max_divisors(M, N):
    # Находит числа из интервала [M, N] с наибольшим количеством делителей.
    max_divisors = 0
    max_numbers = []

    for num in range(M, N + 1):
        current_divisors = count_divisors(num)
        if current_divisors > max_divisors:
            max_divisors = current_divisors
            max_numbers = [num]
        elif current_divisors == max_divisors:
            max_numbers.append(num)

    return max_numbers


M = int(input("Введите начало интервала (M): "))
N = int(input("Введите конец интервала (N): "))

# Находим числа с максимальным количеством делителей
max_numbers = find_numbers_with_max_divisors(M, N)

print(f"Числа из интервала [{M}, {N}] с наибольшим количеством делителей:")
for num in max_numbers:
    print(num)
