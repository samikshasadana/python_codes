#1
import textwrap
a=input()
x=int(input())
l=[]
b=textwrap.wrap(a,x)
print(b)
for i in b:
    l.append(''.join(set(i)))
print(l)

#2
def cal(n):
    return n*n
    
n1=[1,2,3,4,5]
r=map(cal,n1)
print(r)
ns=set(r)
print(ns)

#3
n= int(input())
j=1
for i in range(n+1):
    j=1
    for k in range(i):
        print(j,end=' ')
        j=j+1
    if(j>1):
        for r in range(i-1):
            print(j-2,end=' ')
            j=j-1
    print()
    
#4
'''
m=int(input())
n=int(input())
a=set()
b=set()
l=[]
for i in range(m):
    x=int(input())
    l.append(x)
print(l)
for r in range(n):
    x=int(input())
    a.add(x)
for r in range(n):
    x=int(input())
    b.add(x)
print(a)
print(b)
for i in range(len(l)):
    x=l[0]
    if i in l:
        x=x+1
        print("all element in set a found in list ",x)
    else:
         print("all element in set a not  found in list ",x-1)
    if b in l:
         print("all element in set b found in list ",x)
    else:
         print("all element in set b not  found in list ",x-1)
        
'''
