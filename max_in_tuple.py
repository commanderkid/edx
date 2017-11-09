tup = (1, 4, 6, [1, 4, [5], 8, (1, 4, 5, (8))], 8, [[4, 1, 5], [2], 5], (9,), [1, [2, [3, (4, 5)], 1, 2, 7]], 5)
# make recursion there
def max_tuple(x, l = []):
    for i in x:
        if type(i) == int:
            l.append(i)
        else:
            max_tuple(i, l)
    return max(l)
print(max_tuple(tup))
