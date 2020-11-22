import math

integer = 49
negative_integer = -35
# 49 <class 'int'> -35 <class 'int'>
print(integer, type(integer), negative_integer, type(negative_integer))

# 11111111111111111111111111111111111111111111111111111111111 <class 'int'>
large_integer = 11111111111111111111111111111111111111111111111111111111111
print(large_integer, type(large_integer))

# 3.3333333333333335 <class 'float'>
n = 3.33333333333333333333333
print(n, type(n))

# 3.141592653589793 <class 'float'>
# 2.718281828459045 <class 'float'>
print(math.pi, type(math.pi))
print(math.e, type(math.e))

# 0.3333333333333333 <class 'float'>
x = 1/3
print(x, type(x))

# 7 <class 'int'>
# 17 <class 'int'>
# 9 <class 'int'>
bi = 0b111
print(bi, type(bi))
he = 0x11
print(he, type(he))
oc = 0o11
print(oc, type(oc))

# 0b111 <class 'str'>
# 0x11 <class 'str'>
# 0o11 <class 'str'>
print(bin(7), type(bin(7)))
print(hex(17), type(hex(17)))
print(oct(9), type(oct(9)))

# 0xf <class 'str'>
print(hex(0b1111), type(hex(0b1111)))
