x = 10

# odd
if x % 2 == 0:
    print('odd')
else:
    print('evan')

# x equals 10
if x > 10:
    print('x bigger than 10')
elif x < 10:
    print('x less than 10')
else:
    print('x equals 10')


ACTUALLY_RELEASE_YEAR = 1991
inputYear = int(input("please guess the python release year:"))
if inputYear > ACTUALLY_RELEASE_YEAR:
    print('maybe earlier')
elif inputYear < ACTUALLY_RELEASE_YEAR:
    print('maybe later')
else:
    print('right!')
