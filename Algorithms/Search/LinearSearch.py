def LinearSearch(array: list, item):
    for index, element in enumerate(array):
        if element == item:
            return index
    return -1


integer_list = list(range(1, 101))

item = 40

found_at = LinearSearch(integer_list, item)

print(found_at)

# print(integer_list)
