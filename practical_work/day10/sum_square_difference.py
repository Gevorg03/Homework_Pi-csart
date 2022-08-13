"""Find the difference of square_of_sum and sum_of_square"""

def sum_square_difference(n):
    square_of_sum = 0
    sum_of_square = 0
    for i in range(1, n + 1):
        square_of_sum += i
        sum_of_square += i * i
    square_of_sum **= 2
    return square_of_sum - sum_of_square
print(sum_square_difference(100))
