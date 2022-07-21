#Find the sum of number's digits

#The first solution
def get_sum(num):
    sum = 0
    while num != 0:
        n = num % 10
        sum += n
        num //= 10
    return sum
num = int(input("Input a number: "))
print("Sum =", get_sum(num))

#The second solution
def get_sum(num):
    sum = 0
    for el in num:
        sum += int(el)
    return sum
num = input("Input a number: ")
print("Sum =", get_sum(num))
