l=['hello','world','rishi']
l2=['python','india','kemni']
l3=[]
s=len(l)
for i in range(s):
    for j in range(s):
        l3.append(l[i]+l2[j])
print(l3)

l4=[]
for x in l:
    l4.append(x[0])
print(l4)

l=['with','hello','bag','world']
l2=[]
n=int(input("enter no. of list  elements"))
for i in range(n):
    x=(input("enter list  elements"))
    l2.append(x)
    
l2.sort()
print(l2)

s=(input("enter string"))
l=(s.split(','))
print(l)
l.sort()
print(l)

s=(input("enter string"))
l=(s.split(','))
print(l)
print(tuple(l))
s=(input("enter string"))
q=s.upper()
print(q)
