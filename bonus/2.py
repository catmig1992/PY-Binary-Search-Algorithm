def binary_search(data, el):
    first = 0
    last = len(data) - 1

    while first <= last:
        mid = (first + last)//2

        if data[mid] == el:
            return mid
        else:
            if el < data [mid]:
                last = mid - 1
            else:
                first = mid + 1

    return -1

test_list = [ 2, 4, 5, 6, 7, 9, 10, 22, 44, 67, 88 ]
print(binary_search(test_list, 2))
print(binary_search(test_list, 4))
print(binary_search(test_list, 5))
print(binary_search(test_list, 6))
print(binary_search(test_list, 7))
print(binary_search(test_list, 9))
print(binary_search(test_list, 99))

