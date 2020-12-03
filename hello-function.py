def sum(the_list_of_numberic):
    count = 0
    for i in the_list_of_numberic:
        count += i
    return count

# 45
print(sum(range(10)))
# 45
print(sum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

def join(a, b):
    return a + b

# 3
print(join(1, 2))
# xy
print(join("x", "y"))
