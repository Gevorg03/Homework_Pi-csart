"""Selection sort"""

def selection_sort(lst: list):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


print(selection_sort([5, -7, 12, -3, 1, -3]))
