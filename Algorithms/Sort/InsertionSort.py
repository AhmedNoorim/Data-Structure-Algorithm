# insertion sort
from typing import List


def insertion_sort(array: List[int]):  # defining array is an integer list

    # traversing from index 1, assuming index 0 is already sorted
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]  # assigning value to its previous index
            j -= 1

        array[j + 1] = key


array = [50, 20, 17, 5, 1, 35, 47, 27]

print("Array:", array)

insertion_sort(array)

print("InsertionSort,\nSorted Array:", array)
