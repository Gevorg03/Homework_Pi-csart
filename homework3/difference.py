"""Calculate the difference of (1^2 + 2^2 + … + 100^2) and (1+...+100)^2"""

def difference():
    sum = 0
    sum_square = 0
    for i in range(101):
        sum += i
        sum_square += i * i
    return sum_square - sum
print(f"Difference is {difference()}")
