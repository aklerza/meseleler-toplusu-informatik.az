x,y=int(input()),int(input())
if x<y:
    x,y = (x+y)/2, y*2
else:
    y,x = (x+y)/2, y*2
print(x, y)
