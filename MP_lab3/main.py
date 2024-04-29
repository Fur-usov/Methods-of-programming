import numpy as np
import time
import scipy.stats as stats
import timeit
from nistrng import *

# Создаем таймер
timer = timeit.default_timer

# 1. Модифицированный метод генерации псевдослучайных чисел
def modified_random_method_1(n, a=1103515245, c=12345, d=2342421, m=2**32):
    x = int(time.time())  # начальное значение (seed) основано на текущем времени
    random_numbers = []
    for _ in range(n):
        x = (a * x + c) % m + d
        random_numbers.append(x % 5000)  # ограничиваем диапазон от 0 до 5000
    return random_numbers

def modified_random_method_2(n):
    return np.random.randint(0, 5000, size=n)  # используем метод Мерсенна-Твистера


# 2. Генерация выборок
samples_1 = [modified_random_method_1(1000) for _ in range(20)]
samples_2 = [modified_random_method_2(1000) for _ in range(20)]


# 3. Вычисление статистических показателей
for i, sample in enumerate(samples_1):
    print(f"Sample {i+1} (Method 1): Среднее = {np.mean(sample)}, Отклонение = {np.std(sample)}, Коэффицент вариации = {np.std(sample)/np.mean(sample)}")

for i, sample in enumerate(samples_2):
    print(f"Sample {i+1} (Method 2): Среднее = {np.mean(sample)}, Отклонение = {np.std(sample)}, Коэффицент вариации = {np.std(sample)/np.mean(sample)}")



# 4. Проверка на равномерность и случайность
for i, sample in enumerate(samples_1):
    frequencies, _ = np.histogram(sample, bins=np.arange(5001))
    print(f"Выборка {i+1} (метод 1): Хи-квадрат не отвергается с вероятностью = {stats.chisquare(frequencies)[1]}")

for i, sample in enumerate(samples_2):
    frequencies, _ = np.histogram(sample, bins=np.arange(5001))
    print(f"Выборка {i+1} (метод 2): Хи-квадрат не отвергается с вероятностью = {stats.chisquare(frequencies)[1]}")



# 5. Проверка с помощью тестов NIST и/или Diehard
for samples in [samples_1[:5], samples_2[:5]]:
    for i, sample in enumerate(samples):

        binary_sequence: np.ndarray = pack_sequence(samples)
        eligible_battery: dict = check_eligibility_all_battery(binary_sequence, SP800_22R1A_BATTERY)

        print(f'Eligible test from NIST-SP800-22r1a for sample {i}:')
        for name in eligible_battery.keys():
            print("-" + name)
        # Test the sequence on the eligible tests
        results = run_all_battery(binary_sequence, eligible_battery, False)
        # Print results one by one
        print("Test results:")
        for result, elapsed_time in results:
            if result.passed:
                print("- PASSED - score: " + str(np.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")
            else:
                print("- FAILED - score: " + str(np.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")

# 6. Измерение времени генерации
for n in [1000, 10000, 100000, 1000000]:
    start = timer()
    modified_random_method_1(n)
    print(f"Time for generating {n} numbers using Method 1: {timer() - start}")

    start = timer()
    modified_random_method_2(n)
    print(f"Time for generating {n} numbers using Method 2: {timer() - start}")

    start = timer()
    np.random.randint(0, 5000, size=n)
    print(f"Time for generating {n} numbers using numpy: {timer() - start}")

