"""Find out, if the number is palindrome or no"""

def is_palindrome(number):
    for i in range(len(number) // 2):
        if number[i] != number[-(i+1)]:
            return False
    return True
number = input("Please, enter a number: ")
print(is_palindrome(number))
