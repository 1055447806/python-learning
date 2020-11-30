import math

s = f"the pi value is: {math.pi} and increment 1: {math.pi + 1}"
# the pi value is: 3.141592653589793 and increment 1: 4.141592653589793
print(s)

name = "Gary"
age = 100
s = "Hello {}, you are so old {}".format(name, age)
# Hello Gary, you are so old 100
print(s)

salary = 9999999999.999
s = "My name is %s, i am %d years old, and my salary: %f" %(name, age, salary)
# My name is Gary, i am 100 years old, and my salary: 9999999999.999001
print(s)
