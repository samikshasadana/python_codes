a=int(input("enter a"))
b=int(input("enter b"))
c=0
s=0
l=[]
if(b>a):
    for i in range(a,b+1):
        f=i
        c=0
        while(i!=0):
            rem=i%10
            if(rem%2==0):
                c=c+1
            i=i//10
        if(c==4):
                l.append(f)
else:
    for i in range(b,a+1):
        f=i
        c=0
        while(i!=0):
            rem=i%10
            if(rem%2==0):
                c=c+1
            i=i//10
        if(c==4):
                l.append(f)
    s=s+1
if(s>0):
    print(l)
else:
    l.reverse()
    print(l)
    
