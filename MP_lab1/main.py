import csv
import datetime
from datetime import datetime
import time

# Урусов Фёдор СКБ211
# варинат 23
# в) Сортировка простыми вставками
# д) Пирамидальная сортировка
# ж) Сортировка слиянием


#нужен ли вывод в консоль всех объектов
IsPrinted = False

def line():
    print('-' * 100)

class Ship:
    def __init__(self, name, date, country, ship_type, captain):
        self.name = name
        self.date = date
        self.country = country
        self.ship_type = ship_type
        self.captain = captain

    def __lt__(self, other):
        if self.date < other.date:
            return True
        elif self.date > other.date:
            return False
        else:
            if self.name < other.name:
                return True
            elif self.name > other.name:
                return False
            else:
                if self.ship_type < other.ship_type:
                    return True
                else:
                    return False


    def __gt__(self, other):
        if self.date > other.date:
            return True
        elif self.date < other.date:
            return False
        else:
            if self.name > other.name:
                return True
            elif self.name < other.name:
                return False
            else:
                if self.ship_type > other.ship_type:
                    return True
                else:
                    return False


    def __ge__(self, other):
        if self.date >= other.date:
            return True
        elif self.date < other.date:
            return False
        else:
            if self.name >= other.name:
                return True
            elif self.name < other.name:
                return False
            else:
                if self.ship_type >= other.ship_type:
                    return True
                else:
                    return False

    def __le__(self, other):
        if self.date <= other.date:
            return True
        elif self.date > other.date:
            return False
        else:
            if self.name <= other.name:
                return True
            elif self.name > other.name:
                return False
            else:
                if self.ship_type <= other.ship_type:
                    return True
                else:
                    return False

    def __eq__(self, other):
        if self.date != other.date:
            return False
        if self.name != other.name:
            return False
        if self.ship_type != other.ship_type:
            return False
        return True

    def pr(self):
        print(f"{self.name}, {self.date}, {self.country}, {self.ship_type}, {self.captain}", end="")
        print()


# сортировка простыми вставками
def sort_insert(lst, column=0):
    N = len(lst)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break
    return lst


# пирамидальная сортировка
def heapify(lst, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[i] < lst[left]:
        largest = left

    if right < n and lst[largest] < lst[right]:
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)


def heap_sort(lst):
    n = len(lst)

    for i in range(n, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

    return lst


# сортировка слиянием
def merge_list(a, b, column=0):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


# функция деления списка и слияния списков в общий отсортированный список

def split_and_merge_list(a):
    N1 = len(a) // 2
    a1 = a[:N1]  # деление массива на два примерно равной длины
    a2 = a[N1:]

    if len(a1) > 1:  # если длина 1-го списка больше 1, то делим дальше
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:  # если длина 2-го списка больше 1, то делим дальше
        a2 = split_and_merge_list(a2)



    return merge_list(a1, a2)  # слияние двух отсортированных списков в один


# ввод данных из файла
unsorted_data = list()
with open('ships_5000.csv', encoding="utf-8") as file:
    next(file)
    for row in file:
        r = row.strip().split(",")
        w = Ship(r[0], datetime.strptime(r[1], "%d-%m-%Y"), r[2], r[3], r[4])
        unsorted_data.append(w)

#делаем три набора данных
unsorted_data_1 = unsorted_data_2 = unsorted_data_3 = unsorted_data.copy()
print(f'Длина списка: {len(unsorted_data)}')

line()
print('\nНе сортированные данные')
# Вывод изначальных данных
for i in unsorted_data:
    if IsPrinted:
        i.pr()
line()

print('\n')

line()
print('Сортировка вставками')
start_time1 = time.time()  # Запоминаем время начала выполнения
sorted_data_1 = sort_insert(unsorted_data_1)
end_time1 = time.time()  # Запоминаем время окончания выполнения
print(f'Длина списка: {len(unsorted_data_1)}')
time1 = end_time1 - start_time1
print(f"Время выполнения: {time1} секунд")
for i in sorted_data_1:
    if IsPrinted:
        i.pr()
line()

print("\n")

line()
print('Пирамидальная сортировка')
start_time2 = time.time()  # Запоминаем время начала выполнения
sorted_data_2 = heap_sort(unsorted_data_2)
end_time2 = time.time()  # Запоминаем время окончания выполнения
print(f'Длина списка: {len(unsorted_data_2)}')
time2 = end_time2 - start_time2
print(f"Время выполнения: {time2} секунд")
for i in sorted_data_2:
    if IsPrinted:
        i.pr()
line()

print("\n")

line()
print('Сортировка слиянием')
start_time3 = time.time()  # Запоминаем время начала выполнения
sorted_data_3 = split_and_merge_list(unsorted_data_3)
end_time3 = time.time()  # Запоминаем время окончания выполнения
time3 = end_time3 - start_time3

print(f'Длина списка: {len(unsorted_data_3)}')
print(f"Время выполнения: {time3} секунд")

for i in sorted_data_3:
    if IsPrinted:
        i.pr()

line()