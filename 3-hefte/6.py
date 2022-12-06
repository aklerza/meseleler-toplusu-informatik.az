n=int(input())
m=[]
while n > 0:
    m.append(n % 10)
    n //= 10
m.reverse()
arr=[]
for i in range(0,len(m)):
    if m[i] != 1 and m[i] != 5:
        arr.append(m[i])
eded=0
for i in range(0,len(arr)):
    eded += arr[i]*(10**(len(arr)-1-i))
print(eded)
