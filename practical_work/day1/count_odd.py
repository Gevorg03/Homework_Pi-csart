"""Calculate the count of odds in range"""

def odd(start, end):
    count = 0
    for i in range(start, end+1):
        if i % 2 == 1:
            count += 1
    return count
print(odd(3, 7))
