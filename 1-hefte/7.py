n=int(input())
if n >= 100 and n < 1000:
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    eded = b*100 + a*10 + c
    print(eded)
