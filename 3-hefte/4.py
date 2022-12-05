n=int(input())
m=[]
while n > 0:
    m.append(n%10)
    n//=10
m.sort(reverse=True)
eded=0
for i in range(0,len(m)):
    eded+=m[i]*(10**(len(m)-1-i))
print(eded)
