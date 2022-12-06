n=int(input())
m=[]
while n > 0:
    m.append(n%10)
    n//=10
m.reverse()
maksimum = max(m)
say = m.count(maksimum)
print(say)
