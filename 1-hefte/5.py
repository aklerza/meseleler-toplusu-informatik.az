n=int(input())
if n >= 100 and n < 1000:
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    eded = c *100 + b * 10 + a
    print(eded)
