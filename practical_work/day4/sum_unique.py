"""Find the sum of numbers, that are repeted in list only one time"""

def sum_unique(lst: list):
    sum = 0
    for el in lst:
        if lst.count(el) == 1:
            sum += el
    return sum
print(sum_unique([1, 2, 3, 2, 3, 5]))
