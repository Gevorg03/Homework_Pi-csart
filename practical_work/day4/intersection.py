"""find the same repeted numbers in two list"""

def intersect(lst1, lst2):
    intersect_lst = []
    for el_lst1 in lst1:
        for el_lst2 in lst2:
            if el_lst1 == el_lst2:
                intersect_lst.append(el_lst2)
    return intersect_lst
print(intersect([1, 2, 3], [2, 3, 4]))
