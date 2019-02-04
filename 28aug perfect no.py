l=[]
x=int(input())
y=x
for i in range(1,int(x/2)+1):
        if (x%i==0):
            l.append(i)
print(l)
if(sum(l)==x):
    print('mr.perfect sir...!!!')
else:
    print('not perfect no. sorry')

#2
s=input('enter string')
k=int(input('enter no.'))
for i in range(len(s)//k):
     x=s[0:4]
     r=[]
     for j in range(len(x)):
         if(x[j]==x[j+1]):
             r.append(x[j])
         else:
              r.append(x[j])
         print(r)
         r=[]
             
