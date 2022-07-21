def fibonacci_recursive(n):
    #Find nth member in sequence of fibonacci

    if n <= 1:
        return n
    return (fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2))
n = int(input("Input a number: "))
print(f"Fibonacci's {n}th member is {fibonacci_recursive(n)}")
