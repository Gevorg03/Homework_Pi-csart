"""Calculate the count of words, that are seen in the .txt file"""

f = open('text.txt', 'r')
dct = {}
for line in f:
    lst = line.split()
    for el in lst:
        if el not in dct.keys():
            dct[el] = lst.count(el)
        else:
            pass
print(dct)
