n=int(input())
cem = 0
hasil = 1
while n > 0:
    cem += n % 10
    hasil *= n % 10
    n //= 10

print(cem ,hasil)
