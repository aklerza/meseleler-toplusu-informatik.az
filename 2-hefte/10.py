a=int(input())
b=int(input())
c=int(input())
if a == b and b == c or (c == a and b == a):
    print(3)
elif a == b and b != c or (c == a and b != a):
    print(2)
else:
    print(0)
