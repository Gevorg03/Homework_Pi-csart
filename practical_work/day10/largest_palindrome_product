"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

def is_palindrome_3digit():
    n = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            p = i * j
            str_p = str(p)
            if str_p == str_p[::-1]:
                n = max(n, p)
    return n
print(is_palindrome_3digit())
