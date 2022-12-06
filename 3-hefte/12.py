n=int(input())
m=[]
while n > 0:
    m.append(n%10)
    n//=10
tek_ededler = [1,3,5,7,9]
say=0
for i in tek_ededler:
    say+=m.count(i)
print(say)
