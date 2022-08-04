def digit(num):
    #Find the differene of digit's sum and digit's multiplication
    
    sum = 0
    multiple = 1
    while num != 0:
        n = num % 10
        sum += n
        multiple *= n
        num //= 10
    return multiple - sum
num = int(input("Input a number: "))
print("Result =", digit(num))
