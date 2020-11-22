import sys

# comments
print(sys.argv[0],"is start!")

if len(sys.argv)<3:
    print("arguments length less 3")
    print("actually the length is ",len(sys.argv))
else:
    """
    input args
    """
    name = sys.argv[1]
    age = int(sys.argv[2])
    print(f"hello {name}, you are {age}")

n = int(input("input n:"))
for i in range(1,11):
    print(i,"*",n,"=",i*n)
print("process completed and successfully!")
