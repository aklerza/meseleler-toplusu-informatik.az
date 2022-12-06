n=int(input())
m=[]
while n > 0:
    m.append(n%10)
    n//=10
#reverse() istifadə etmədim. çünki ədədlər onsuz da soldan sağa əlavə edilir yuxarıdakı dövrün nəticəsinə əsasən.
eded=0
for i in range(0,len(m)):
    eded+=m[i]*(10**(len(m)-1-i))
print(eded)
