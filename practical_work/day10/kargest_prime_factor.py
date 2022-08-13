"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

def largest_prime_factor(number):
    n = 2
    while n < number:
        while number % n == 0:
            number //= n
        n += 1
    return number
print(largest_prime_factor(600851475143))
