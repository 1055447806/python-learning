def sum(x, y = 10):
    return x + y

# 20
print(sum(10))

# 30
print(sum(10,20))

def var_sum(*args):
    sum = 0
    for e in args:
        sum += e
    return sum

# 60
print(var_sum(10, 20, 30))
