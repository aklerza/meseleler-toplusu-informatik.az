n=int(input())

if n >= 100 and n < 1000:
    a = n // 100
    b = (n - a*100) // 10
    c = (n - a*100) % 10
    print(a, b, c)
