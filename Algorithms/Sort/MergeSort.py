# Merge Sort
from typing import List


def merge_sort(array: List[int]):

    if len(array) > 1:
        mid = len(array) // 2

        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):

            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1

            k += 1

        # if any item left
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(left_half):
            array[k] = right_half[j]
            j += 1
            k += 1


array = [50, 20, 17, 5, 1, 35, 47, 27]

print("Array:", array)

merge_sort(array)

print("\nMergeSort,\nSorted Array:", array)
