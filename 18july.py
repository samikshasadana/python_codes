def disp():
    print("hi master rishi")
r=5
print(r)
disp();
import random
def disp1():
    a=random.randint(10,20)
    return a;
d=disp1()
print(d)

def disp2(l,b):
    a=l*b
    print(a)
b=int(input("enter l"))
c=int(input("enter b"))
disp2(b,c)

def disp3(l,b):
    a=l*b
    s="rishi is great ... sir please be positive and stay relaxed"
    p=l-b
    return (a,s)
b=int(input("enter l"))
c=int(input("enter b"))
f=disp3(b,c)
print(f)
