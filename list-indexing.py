digits = [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
print(digits)

letters = ['a', 'b', 'c', 'd']
# ['a', 'b', 'c', 'd']
print(letters)

mixed = [1, 2, 3, 'a', 'b', [1, 2, 3, 'a', 'b', 'c']]
# [1, 2, 3, 'a', 'b', [1, 2, 3, 'a', 'b', 'c']] 6
print(mixed, len(mixed))

lists = [1, 2, 3, 4, 5, 6]
# 1
print(lists[0])
# 5
print(lists[4])
# 6
print(lists[-1])
# 1
print(lists[-6])
# [1, 2, 3, 4, 5, 6]
print(lists[0:6])
# [1, 2, 3, 4, 5, 6]
print(lists[:6])
# [1, 2, 3, 4, 5, 6]
print(lists[0:])
# [3, 4, 5, 6]
print(lists[2:len(lists)])
# [3, 4, 5, 6]
print(lists[-4:])
# [3, 4]
print(lists[2:-2])
# [1, 2, 3, 4, 5, 6]
print(lists[:])
# [1, 2, 3, 4, 5, 6]
print(lists[0:6:1])
# [1, 3, 5]
print(lists[0:6:2])
# [1, 4]
print(lists[0:6:3])

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = l1 + l2
# [1, 2, 3, 'a', 'b', 'c']
print(l3)

lists = [1, 2, 3, 4, 5]
lists[1] *= 10
# [1, 20, 3, 4, 5]
print(lists)
lists.append(6)
# [1, 20, 3, 4, 5, 6]
print(lists)
