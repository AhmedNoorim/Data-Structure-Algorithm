# Binary Search

integer_list = list(range(1, 101))

item = 76


# Binary Search With Loop
def BinarySearchLoop(array: list, item):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == item:
            return mid

        elif array[mid] > item:
            right = mid - 1

        elif array[mid] < item:
            left = mid + 1

    return -1


found_at = BinarySearchLoop(integer_list, item)

print("BinarySearchLoop,\nFound At:", found_at)


# Binary Search With Recursion
def BinarySearchRecursion(array: list, item, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if array[mid] == item:
        return mid
    elif array[mid] > item:
        return BinarySearchRecursion(array, item, left, mid - 1)
    elif array[mid] < item:
        return BinarySearchRecursion(array, item, mid + 1, right)


found_at = BinarySearchRecursion(integer_list, item, 0, 99)

print("BinarySearchRecursion,\nFound At:", found_at)
