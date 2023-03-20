import random

def make_random_list(size = 10, min = -1000, max = 1000):
    return [random.randint(min, max) for n in range(size)]

def recursive_bsearch(data, target):
    print(f"data is {data}")
    if len(data) == 0:
        return False
    else:
        mid = len(data)//2

        print(f"mid is {mid}")
        if data[mid] == target:
            return True
        else:
            if target < data[mid]:
                return recursive_bsearch(data[:mid], target)
            else:
                return recursive_bsearch(data[mid +1:], target)
            
test_list = make_random_list(50, 0, 100)
# test_list = [ 5, 8, 10, 25, 35, 40, 44 ]
print(recursive_bsearch(sorted(test_list), 35))

