'''s=input()
u=l=0
for c in s:
    if c.isupper():
        u=u+1
    if c.islower():
        l=l+1
print (u)
print(l)
s=str(input())
n1=int(s)
n2=int(2*s)
n3=int(3*s)
n4=int(4*s)
a=n1+n2+n3+n4
print(a)'''

s=input()
l=[]
l=s.split(" ")
l1=sorted(l)
a={}
for i in l1:
    c=0
    for j in l:
        if i==j:
            c=c+1
    a[i]=c
for i in a:
    print(i,a[i])
