"""Calculate the square of numbers and add in new list by sorted"""

lst = [1, 2, 10, 5, 3]
def foo(lst):
    square_lst = []
    for el in lst:
        square_lst.append(el**2)
    return sorted(square_lst)
print(foo(lst))
