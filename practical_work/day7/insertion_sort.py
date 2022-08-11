"""Insertion sort"""

def insertion_sort(lst: list):
    for i in range(1, len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
print(insertion_sort([-7, 5, -7, 12, -3, 1, -3]))
