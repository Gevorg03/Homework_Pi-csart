def divided_index(lst):
    #Find the count of numbers, that are divided their index without remainder

    count = 0
    for i in range(1, len(lst)):
        if lst[i] % i == 0:
            count += 1
    return count
print(divided_index([1, 2, 4, 15, 23]))
