n=float(input("enter salary"))
if(n>500000):
    print("tax is",n*0.3)
elif(n>300000)&(n<=500000):
    print("tax is",n*0.2)
elif(n>150000)&(n<=300000):
    print("tax is",n*0.1)
elif(n<=150000):
    print(" no tax")

a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
if((b*b)<(4*a*c)):
    print("imaginary roots")
elif((b*b)>=(4*a*c)):
    print("real roots")
else:
    print("b*b=4ac")




x=int(input("enter a"))
y=int(input("enter b"))
small=0;
if(x>y):
small=x
else:
    small=y

for i in range(1,small+1):
    if(x%i==0)&(y%i==0):
        print("hcf",i)
    

