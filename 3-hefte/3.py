n=int(input())
printed=False
while n > 1:
    if n % 2 == 0:
        n = n//2
    else:
        print("NO")
        printed=True
        break

if not printed:
    if n == 1:
        print("YES")
    else:
        print("NO")
