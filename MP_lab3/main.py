import numpy as np
import time
import scipy.stats as stats
import timeit

# Создаем таймер
timer = timeit.default_timer

# 1. Модифицированный метод генерации псевдослучайных чисел
def modified_random_method_1(n, a=1103515245, c=12345, m=2**32):
    x = int(time.time())  # начальное значение (seed) основано на текущем времени
    random_numbers = []
    for _ in range(n):
        x = (a*x + c) % m
        random_numbers.append(x % 5000)  # ограничиваем диапазон от 0 до 5000
    return random_numbers

def modified_random_method_2(n):
    return np.random.randint(0, 5000, size=n)  # используем метод Мерсенна-Твистера

# 2. Генерация выборок
samples_1 = [modified_random_method_1(1000) for _ in range(20)]
samples_2 = [modified_random_method_2(1000) for _ in range(20)]

# 3. Вычисление статистических показателей
for i, sample in enumerate(samples_1):
    print(f"Sample {i+1} (Method 1): Mean = {np.mean(sample)}, Std Dev = {np.std(sample)}, CoV = {np.std(sample)/np.mean(sample)}")

for i, sample in enumerate(samples_2):
    print(f"Sample {i+1} (Method 2): Mean = {np.mean(sample)}, Std Dev = {np.std(sample)}, CoV = {np.std(sample)/np.mean(sample)}")


# 4. Проверка на равномерность и случайность
for i, sample in enumerate(samples_1):
    print(f"Sample {i+1} (Method 1): Chi-square test p-value = {stats.chisquare(sample)[1]}")

for i, sample in enumerate(samples_2):
    print(f"Sample {i+1} (Method 2): Chi-square test p-value = {stats.chisquare(sample)[1]}")

# 5. Проверка с помощью тестов NIST и/или Diehard
# Этот шаг требует специализированных библиотек или внешних утилит, которые не включены в стандартную библиотеку Python.

# 6. Измерение времени генерации
for n in [1000, 10000, 100000, 1000000]:
    start = time.time()
    modified_random_method_1(n)
    print(f"Time for generating {n} numbers using Method 1: {time.time() - start}")

    start = time.time()
    modified_random_method_2(n)
    print(f"Time for generating {n} numbers using Method 2: {time.time() - start}")

    start = time.time()
    np.random.randint(0, 5000, size=n)
    print(f"Time for generating {n} numbers using numpy: {time.time() - start}")

