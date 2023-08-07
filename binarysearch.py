import math


def binary_search(listinput: list, target):
    listinput.sort()
    low = 0
    high = len(listinput) - 1
    found = False
    operation = math.ceil

    while found is not True:
        mid = operation((low + high) / 2)
        element = listinput[mid]
        if high - low == 0 and element != target:
            print(f"{target} not found")
            break
        if element == target:
            found = True
            print(f"{element} found at index {mid}")
        elif element > target:
            high = mid - 1
        elif element < target:
            low = mid + 1
