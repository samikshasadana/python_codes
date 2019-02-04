a=()
print(a)
a=('r','i','s','h','i')
print(a[2])
print(len(a))
t=(2,1,0,3,1,9,9,9)
t1=("love","you")
print(t+t1)
t3=(t,t1)
print(t3)
t4=("rishi",)*3
print(t4)
for i in range(0,4):
    print(t1)
print(max(t))
print(min(t))
print('i' in a)
print(a.index('r'))
print(a.count('i'))
r=()
a=int(input("enter no. of elements in tuple"))
r=(1,2,3,4,5,6,78,90,0)
a=(20,30)
print(r)
#a=()
print(r[4])
print(r[-4])
(a,r)=(r,a)
print(a,r)
tup=()
k=(-10,0,9,-1,-2,3,7,-123)
for i in k:
    if(i>0):
        tup=tup+(i,)
print(tup)

def sum(*args):
    sum=0
    for i in args:
        if(i>0):
            sum=sum+i
    return sum
l=[1,2,3,4,5,6,1,1,2,3,4,2,2,3,4,3]
r=[]
l.sort()
print(l)
for i in l:
    if i not in r:
        r.append(i)
print(r)
    
