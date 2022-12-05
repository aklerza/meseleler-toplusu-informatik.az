#Qara 1, Ag 0

a1=int(input())
a2=int(input())
b1=int(input())
b2=int(input())

def colorver(a,b):
    if b % 2 == 0:
        if a % 2 == 0:
            return 1
        else:
            return 0
    else:
        if a % 2 != 0:
            return 1
        else:
            return 0
            
if colorver(a1,a2) == colorver(b1,b2):
    print("YES")
else:
    print("NO")
