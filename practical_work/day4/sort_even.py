"""Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition."""

def sort_even(lst: list):
    count = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i], lst[count] = lst[count], lst[i]
            count += 1
    return lst
print(sort_even([6, 3, 5, 2, 4]))
