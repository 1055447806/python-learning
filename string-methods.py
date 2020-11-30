s = "gary"
# Gary
print(s.capitalize())

s = "GARY"
# Gary
print(s.capitalize())

s = "hello GARY"
# hello gary
print(s.lower())

s = "hello GARY"
# HELLO GARY
print(s.upper())

s = "hello world"
# True
print(s.startswith(s))
# True
print(s.endswith(s))

s = "hello world"
# o world
print(s.strip("hell"))
# hello w
print(s.strip("orld"))

s = "hello world"
# he$$o wor$d
print(s.replace("l","$"))

s = "hello world"
# 2
print(s.find("l"))
