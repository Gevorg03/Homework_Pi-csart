"""Calculate the sum of fibonacci members, that don't exceed 4 million and are even"""

sum = 0
lst = [0, 1]
while True:
    if lst[-1] >= 4000000:
        break
    fib = lst[-1] + lst[-2]
    lst.append(fib)
    if fib % 2 == 0:
        sum += fib
print(sum)
