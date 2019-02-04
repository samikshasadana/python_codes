m=int(input("enter m yaar"))
n=int(input("enter n yaar"))
s=0
op=0
if(op==1):
  while(m<=n):
    s=s+1
    m=m+1
print("sum from m to n is %d"%s)
elif(op==2):
    n=int(input("enter no. yaar"))
    while(n!=-1):
        p=0,ne=0,z=0;
        if(n>0):
            p=p+1
        elif(n<0):
            ne=ne+1
        else:
            z=z+1
        n=int(input("enter no. again  yaar and -1 to exit"))
    else:
        print("no. of zeros%d"%z)
        print("no. of positive no.%d"%p)
        print("no. of negative no.s%d"%ne)
