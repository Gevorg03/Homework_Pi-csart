"""Calculate the count of numbers, that are repeted in list usimg dictionary"""

lst = [45, 8, 56, 120, 45, 120]
dictionary = {'count': 0}
for index1 in range(len(lst)):
    for index2 in range(index1+1, len(lst)):
        if lst[index1] == lst[index2]:
            dictionary['count'] += 1
print(dictionary['count'])
