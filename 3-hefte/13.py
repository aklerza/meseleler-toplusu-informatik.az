ededler=[]
k=int(input())

for i in range(10**(k-1), 10**k):
    quvvet = 0
    l=i
    while i > 0:
        reqem = i % 10
        quvvet += reqem**k
        i//=10
    if quvvet == l:
        ededler.append(l)
        
print(ededler)
