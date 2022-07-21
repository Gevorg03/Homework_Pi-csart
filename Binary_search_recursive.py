def binary_search(lst, key, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if lst[mid] == key:
        return mid
    if lst[mid] <= key:
        start = mid + 1
    else:
        end = mid - 1
    return binary_search(lst, key, start, end)
lst = [7, 10, 24, 31, 40]
print(binary_search(lst, 31, 0, len(lst) - 1))
