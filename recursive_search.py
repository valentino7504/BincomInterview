def binary_search(list_to_be_searched, lower, upper, x):
    if upper >= lower:
        middle = (upper + lower) // 2
        if list_to_be_searched[middle] == x:
            return middle
        elif list_to_be_searched[middle] > x:
            return binary_search(list_to_be_searched, lower, middle - 1, x)
        else:
            return binary_search(list_to_be_searched, middle + 1, upper, x)
    else:
        return -1


my_list = [2, 3, 4, 10, 12, 19, 18, 29]
value = 18
located_index = binary_search(my_list, 0, len(my_list) - 1, value)
if located_index != -1:
    print(f"Element is present at index {located_index}")
else:
    print("Element is not in array")
