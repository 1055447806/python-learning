def fun_iterable(iterable):
    l = []
    for e in iterable:
        l.append(e * 2)
    return l

# [2, 4, 6, 8, 10]
print(fun_iterable([1, 2, 3, 4, 5]))

def fun_map(iterable, f):
    l = []
    for e in iterable:
        l.append(f(e))
    return l

def fun_double(e):
    return e * 2

# [2, 4, 6, 8, 10]
print(fun_map([1, 2, 3, 4, 5], fun_double))

# [3, 6, 9, 12, 15]
print(fun_map([1, 2, 3, 4, 5], lambda e: 3 * e))

add = lambda x, y: x + y

# 30
print(add(10, 20))

add = lambda x, y: (
    print("x: ",x),
    print("y: ",y),
    x + y
)

# (None, None, 30)
print(add(10, 20))

# 30
print(add(10, 20)[-1])

def xyz(x):
    return lambda n: n * x

# 200
print(xyz(10)(20))
