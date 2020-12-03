"""
0
10
20
30
40
"""
for i in range(10):
    if i == 5:
        break
    else:
        print(i * 10)

"""
0
10
20
30
40
60
70
80
90
"""
for i in range(10):
    if i == 5:
        continue
    else:
        print(i * 10)

"""
0
10
20
30
40
60
70
80
"""
for i in range(10):
    if i == 5:
        pass
    else:
        print(i * 10)

"""
0
10
20
30
40
50
60
70
80
90
"""
for i in range(10):
    if i == 5:
        pass
    print(i * 10)

"""
outer: 0, inner: 0
outer: 0, inner: 1
outer: 0, inner: 2
outer: 0, inner: 3
outer: 0, inner: 4
"""
outer_break = False
for i in range(10):
    for j in range(10):
        if j == 5:
            outer_break = True
            break
        print(f"outer: {i}, inner: {j}")
    if outer_break:
        break

