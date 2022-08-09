def push_pop(target: list, n):
    lst = []
    for i in range(target[0], target[-1] + 1):
        if i in target:
            lst.append("push")
        else:
            lst.append("push")
            lst.append("pop")
    return lst


print(push_pop([1, 3], 3))
