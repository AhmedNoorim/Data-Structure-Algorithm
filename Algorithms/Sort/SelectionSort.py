# SelectionSort
from typing import List


def selection_sort(array: List[int]):

    for i in range(len(array) - 1):

        min_index = i

        # unsorted portion
        for j in range(i + 1, len(array)):

            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


array = [50, 20, 17, 5, 1, 35, 47, 27]

print("Array:", array)

selection_sort(array)

print("\nSelectionSort,\nSorted Array:", array)
