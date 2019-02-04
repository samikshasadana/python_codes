'''a=int(input("enter 1st no."))
b=int(input("enter 2nd no."))
if(a==b):
    print("equal")
else:
    print("not equal")
    
def vol(c,d,e):
    print(c*d*e)


c=int(input("enter no."))
d=int(input("enter lower range"))
e=int(input("enter upper range"))
if(c in range(d,e)):
    print("its in the range")
else:
    print("not in range")'''

def find(*args):
    sum=0
    c=0
    m=1
    for i in args:
        sum=sum+i
        m=m*i
        c=c+1
    return sum,c,m

def st(a,b):
    c=0
    for i in a:
          c=c+1
          if(i==b):
              print(c)
         
a=input("enter string")
b=input("enter character")
st(a,b)




    
