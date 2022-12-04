n=int(input())
if n >= 1000 and n < 10000:
    a= n//1000
    b= (n//100) % 10
    c= (n//10) % 10
    d= n % 10
    if a != b and b != c and b != d:
        print("YES")
    else:
        print("NO")
