# code your iterative algorithm here
import random

def make_random_list(size = 10, min = -1000, max = 1000):
    return [random.randint(min, max) for n in range(size)]

def binary_search(data, el):
    first = 0
    last = len(data) - 1
    found = False

    sorted_list = sorted(data)

    while first <= last and not found:
        mid = (first + last)//2
        print (f"Scanning from {mid} to {first} or {last}")

        if sorted_list[mid] == el:
            found = True
        else:
            if el < sorted_list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found

unsorted_list = make_random_list(100, 0, 100)

print (binary_search(unsorted_list, 81))

# test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

# print(binary_search(test_list, 12))
