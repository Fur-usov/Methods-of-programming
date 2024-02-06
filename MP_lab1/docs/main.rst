main module
===========

.. automodule:: main
   :members: heapify
   :undoc-members:
   :show-inheritance:

.. py:class:: class Ship
class for working with ships

.. py:method:: <
comparison override

.. py:method:: >
comparison override

.. py:method:: >=
comparison override

.. py:method:: <=
comparison override

.. py:method:: ==
comparison override

.. py:function:: def sort_insert(lst, column=0):
Insert sort implementation

.. code-block:: python

   def sort_insert(lst, column=0):
        N = len(lst)...
        for i in range(1, N):
            for j in range(i, 0, -1):
                if lst[j] < lst[j - 1]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                else:
                    break
        return lst


.. py:function:: def heapify(lst, n, i):
Makes a heap from array

.. code-block:: python

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


.. py:function:: def heap_sort(lst):
Heap sort implementation

.. code-block:: python

    def heap_sort(lst):
        n = len(lst)

        for i in range(n, -1, -1):
            heapify(lst, n, i)

        for i in range(n - 1, 0, -1):
            lst[i], lst[0] = lst[0], lst[i]
            heapify(lst, i, 0)

        return lst

.. py:function:: def merge_list(a, b, column=0):
Merge sort

.. code-block:: python

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


.. py:function:: def split_and_merge_list(a):
The function of dividing the list and merging the lists into a common sorted list

.. code-block:: python

    def split_and_merge_list(a):
        N1 = len(a) // 2
        a1 = a[:N1]  # деление массива на два примерно равной длины
        a2 = a[N1:]

        if len(a1) > 1:  # если длина 1-го списка больше 1, то делим дальше
            a1 = split_and_merge_list(a1)
        if len(a2) > 1:  # если длина 2-го списка больше 1, то делим дальше
            a2 = split_and_merge_list(a2)

        return merge_list(a1, a2)  # слияние двух отсортированных списков в один
