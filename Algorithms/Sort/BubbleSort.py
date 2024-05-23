# Bubble Sort
from typing import List


def bubble_sort(array: List[int]):

    for i in range(len(array) - 1):

        # last i element are already sorted
        for j in range(len(array) - i - 1):

            # picking the 1st element and compare it with its next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


array = [50, 20, 17, 5, 1, 35, 47, 27]

print("Array:", array)

bubble_sort(array)

print("BubbleSort,\nSorted Array:", array)
