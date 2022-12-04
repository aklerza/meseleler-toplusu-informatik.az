n=int(input())
if n >= 1000 and n < 10000:
    a= n//1000
    b= (n//100) % 10
    c= (n//10) % 10
    d= n % 10
    if n % a == 0 and n % b == 0 and n % c == 0 and n % d == 0:
        print("Bölünür.")
    else:
        print("Bölünmür.")
