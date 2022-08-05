"""Calculate the count of symbols in .txt file"""

f = open('file.txt', 'r')
count = 0
for line in f:
    lst = line.split("/n")
    for el in lst:
        count += len(el)
print(count)
