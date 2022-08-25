"""Find the sum of number's digits"""

def get_sum(num):
    sum = 0
    while num != 0:
        n = num % 10
        sum += n
        num //= 10
    return sum
num = int(input("Input a number: "))
print("Sum =", get_sum(num))
