n=int(input())
if n >= 10000 and n < 100000:
    a= n//10000
    b= (n//1000) % 10
    c= (n//100) % 10
    d= (n//10) % 10
    e= n % 10
    if a < b and b < c and c < d and d < e:
        print("Artma sırası ilə düzülüb.")
    else:
        print("Artma sırası ilə düzülməyib.")
