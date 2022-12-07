k=int(input())
m=[]
for n in range(2,k):
    for i in range(2,n+1):
        if n == i:
            m.append(n)
            break
        if n%i == 0:
            break
print(m)
