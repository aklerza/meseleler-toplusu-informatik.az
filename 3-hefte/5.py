import math
n=int(input())
uzunluq = int(math.log10(n))+1
eded = (3*10**(uzunluq)) + n
print(eded)
