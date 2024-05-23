# Bubble Sort
from typing import List


def bubble_sort(array: List[int]):

    for i in range(len(array)):
        key = array[i]

        for j in range(i + 1, len(array)):

            if array[i] > array[j]:
                array[i] = array[j]
                array[j] = key


array = [50, 20, 17, 5, 1, 35, 47, 27]

print("Array:", array)

bubble_sort(array)

print("BubbleSort,\nSorted Array:", array)
