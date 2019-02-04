a=list()
l1=[1,2,3,4,5]
l2=["rishi",2,3,"kemni"]
print(l1)

import random
a=[]
e=[]
o=[]
r=[]
t=[]
n=int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.randint(1,100))
    if(a[j]%2==0):
        e.append(a[j])
    else:
        o.append(a[j])
print("even list is ",e,end=' \n')
print("odd list is ",o,end='\n')
print('Randomised list is: ',a,end='\n')

r=[]
t=[]

s=int(input("Enter number of strings:"))
for i in range(s):
    l=input("enter string")
    r.append(l)

for i in range(s):
    a=r[i]
    if(a[0]==a[-1]):
         t.append(a)
    else:
        print(a,"not part of list")
        
