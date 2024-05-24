# Quick Sort
from typing import List


def partition(array: List[int], left: int, right: int):
    pivot = array[right]
    swap_index = left - 1

    for i in range(left, right + 1):
        if array[i] <= pivot:
            swap_index += 1

            # when swap_index and i is same there is no need to swap
            if swap_index != i:
                array[i], array[swap_index] = array[swap_index], array[i]

    return swap_index


def quick_sort(array: List[int]):  # defining array is an integer list
    left = 0
    right = len(array) - 1

    def quick_sort_recursive(array, left, right):
        if left < right:
            partition_index = partition(array, left, right)
            # sorting left partition
            quick_sort_recursive(array, left, partition_index - 1)
            # sorting right partition
            quick_sort_recursive(array, partition_index + 1, right)

    quick_sort_recursive(array, left, right)


array = [50, 20, 17, 5, 1, 35, 47, 27]

print("Array:", array)

quick_sort(array)

print("\nQuickSort,\nSorted Array:", array)
