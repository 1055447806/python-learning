rge = range(1, 10)
# range(1, 10)
print(rge)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(rge))

rge = range(10)
# range(0, 10)
print(rge)

rge = range(0, 10, 1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(rge))

rge = range(0, 10, 2)
# [0, 2, 4, 6, 8]
print(list(rge))

rge = range(0, 10, 3)
# [0, 3, 6, 9]
print(list(rge))


rge = range(1, 10)
# True
print(3 in rge)
# False
print(30 in rge)
