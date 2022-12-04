n=int(input())
if n >= 100 and n < 1000:
    a = n // 100
    b = (n//10) % 10
    c = n % 10
    if a**3 + b**3 + c**3 == n:
        print("Armstronq")
    else:
        print("Armstronq deyil.")
