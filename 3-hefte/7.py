n=int(input())
m=[]
while n > 0:
    m.append(n%10)
    n//=10
m.reverse()

if m == m[::-1]:
    print("YES")
else:
    print("NO")
