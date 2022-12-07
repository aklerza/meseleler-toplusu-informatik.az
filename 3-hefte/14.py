n=int(input())
m=[]
while n > 0:
    reqem = n % 10
    if reqem != 2 and reqem != 4 and reqem != 6 and reqem != 8:
        m.append(reqem)
    n //= 10
    
m.reverse()

eded=0

for i in range(0,len(m)):
    eded += m[i]*(10**(len(m)-1-i))
    
print(eded)
