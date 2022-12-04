n=int(input())
if n >= 1000 and n < 10000:
    n = str(n).replace("0", "")
    n = str(n).replace("2", "")
    n = str(n).replace("4", "")
    n = str(n).replace("6", "")
    n = str(n).replace("8", "")
    
    # nəyə görə uzatdığımı sorğulamayın :)
    
    print(int(n))
