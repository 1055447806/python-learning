end = 10
i = 0

"""

i:0
i:1
i:2
i:3
i:4
i:5
i:6
i:7
i:8
i:9
do else

"""
while i < end:
    print(f"i:{i}")
    i += 1
else:
    print("do else")
    

ACTUALLY_RELEASE_YEAR = 1991
win = False
while not win:
    inputYear = int(input("please guess the python release year:"))
    if inputYear > ACTUALLY_RELEASE_YEAR:
        print('maybe earlier')
    elif inputYear < ACTUALLY_RELEASE_YEAR:
        print('maybe later')
    else:
        win = True
        print('right!')
else:
    print('you win!')

