a1=int(input())
a2=int(input())
b1=int(input())
b2=int(input())


def mumkun_hallar(a1,a2):
    return [
     [a1-2, a2+1],
     [a1-2, a2-1],
     [a1-1, a2+2],
     [a1-1, a2-2],
     [a1+1, a2+2],
     [a1+1, a2-2],
     [a1+2, a2-1],
     [a1+2, a2+1]
    ]

hallar = mumkun_hallar(a1,a2)
okay=False
for i in range(0,len(hallar)):
    if hallar[i][0] == b1 and hallar[i][1] == b2:
        print("YES")
        okay = True
        break

if not okay:
    print("NO")
