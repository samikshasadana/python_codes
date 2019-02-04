'''#1
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print (','.join(l))

#2
def fact(x):
    if x == 0:
         return 1
    return x * fact(x - 1)
x=int(input())
print(fact(x))

#3
n=int(input())
d={}
for i in range(0,n+1):
    d[i]=i*i
print(d)
#4
x=(input())
l=x.split(",")
t=tuple(l)
print(l)
print(t)

#5
rk=[]
l=[]
c=50
h=30
x=(input())
l=x.split(',')
print(l)
#l=",".join(l)
for i in l:
    q=((2*int(i)*c)/h)**0.5
    rk.append(int(q))
print(rk)

#6
l=[]
k=[]
x=int(input("enter x"))
y=int(input("enter y"))
for i in range(0,x):
    for j in range(y):
        s=i*j
        l.append(s)
    k.append(l)
    l=[]
print(k)

#7
s=input('enter strings')
l=s.split(',')
l.sort()
print(l)


#8
s=input()
s.split(' ')
print(s)
x=s.upper()
print(x)

#9
x=input()
w=x.split(' ')
print(w)
l=[]
l=list(set(w))
print(l)
l.sort()
print(l)

#10

s=(input())
x=[]
l=[]
l=s.split(',')
print(l)
for i in range(len(l)):
    c=l[i]
    if (c%5==0):
      print(c)
    
v=[]
items=[x for x in input().split(',')]
for p in items:
    intp=int(p,2)
    print(intp)
    if not intp%5:
        v.append(p)
print(','.join(v))
#11
l=[]
for i in range(1000,3001):
    x=str(i)
    if ((int(x[0]))%2==0) and (int((x[1]))%2==0) and (int(x[2])%2==0) and (int(x[3])%2==0):
        l.append(x)

print(' '.join(l))
#8 redefined
l = []
while True:
    s = input()
    if s:
        l.append(s.upper())
    else:
        break;
for sentence in lines:
    print(sentence)
# 20
u=int(input())
d=int(input())
l=int(input())
r=int(input())
d=u-d;
d=abs(d)
d2=abs(l-r)
x=(d*d+d2*d2)
x=x**0.5
print(int(x))


s=input()
d=0
l=0
for i in (s):
    if(i.isdigit()):
        d=d+1
    elif(i.isalpha()):
        l=l+1
    else:
        print('OOPS!!!!')
print("digits are",d )
print('letters are',l)
'''
import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
         pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))
