n=int(input())
if n >= 10000 and n < 100000:
    i1, i2 = (n // 10000) % 10, (n //1000) % 10
    s1, s2 = (n // 10) % 10, n % 10
    iCem, sCem = i1+i2, s1+s2
    eded = iCem - sCem
    print(eded)
