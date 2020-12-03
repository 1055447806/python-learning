t = True
f = False
# True
print(t)
# False
print(f)

b1 = 10 < 1
# False
print(b1)

b2 = len("Hello World") == 11
# True
print(b2)

b3 = 10 > 9
# True
print(b3)

b4 = 10 <= 20
# True
print(b4)

b5 = 10 != 20
# True
print(b5)


i = 10
j = 10
# True
print(i == j)
# True
print(i is j)

j = 20
# True
print(i != j)
# True
print(i is not j)

class P:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        print("excute __eq__ method")
        return self.name == other.name and self.age == self.age

p1 = P("Gary",100)
p2 = P("Gary",100)
# 如果重写了 __eq__ 方法，那么 == 判断会使用 __eq__ 方法
# True
print(p1 == p2)
# False
print(id(p1) == id(p2))
# False
print(p1 is p2)
