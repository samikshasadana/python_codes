x=int(input())
y=int(input())
z=int(input())
d=(input())
if(d=='g1'):
    if(y<z):
        print("g3 is expensive costing rs ",z)
    else:
        print("g2 is expensive costing rs ",y)
elif(d=='g2'):
    if(x<z):
        print("g3 is expensive costing rs ",z)
    else:
        print("g1 is expensive costing rs ",x)
elif(d=='g3'):
    if(x>y):
        print("g1 is expensive costing rs ",x)
    else:
         print("g2 is expensive costing rs ",y)
else:
    if(x>y):
        if(x>z):
            print("g1 is expensive costing rs ",x)
        else:
            print("g3 is expensive costing rs ",z)
    elif(y>x):
        if(y>z):
             print("g2 is expensive costing rs ",y)
        else:
            print("g3 is expensive costing rs ",z)
            
         
    
