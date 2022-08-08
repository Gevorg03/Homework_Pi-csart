"""Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums."""

def degree(lst: list):
    max_count = lst.count(lst[0])
    element = lst[0]
    index2 = None
    for el in lst:
        if max_count < lst.count(el):
            max_count = lst.count(el)
            element = el

    index1 = lst.index(element)
    i = len(lst) - 1
    while i >= 0:
        if element == lst[i]:
            index2 = i
            break
        i -= 1

    return [lst[i] for i in range(index1, index2 + 1)]


print(degree([1, 2, 2, 3, 1, 4, 2, 3]))
