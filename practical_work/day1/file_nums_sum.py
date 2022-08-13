"""Return the sum of numbers, that are kipped in .txt file"""

f = open('file.txt', 'r')
sum = 0
for line in f:
    lst = line.split()
    for el in lst:
        sum += int(el)
print(sum)
