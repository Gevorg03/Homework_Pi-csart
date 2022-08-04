lst = []
lst.append(0)
lst.append(1)
def fib(n):
    if n <= 1:
        return lst[n]
    lst.append(fib(n-1) + fib(n-2))
    return lst[len(lst)-1]
print(fib(6))
