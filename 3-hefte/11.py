n=int(input())
for i in range(1, n):
    m=[]
    r=i
    while r > 0:
        m.append(r % 10)
        r //= 10
    m.reverse()
    k=m.copy()
    k.sort()
    if m == k:
        print(i)
