""""Bubble sort"""

def bubble_sort(lst: list):
    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
                swapped = True
        if not swapped:
            break
    return lst


print(bubble_sort([5, -7, 12, -3, 1]))
