
s=(input("enter no.s"))
l=s.split(',')
print(l)
l.sort()
print(l)

#l=input()
l='chitkara'
c = {l[i].upper(): l[i+2]  for i in  range(len(l)-2 )}
print(c)

y=""
q=""
e={}
d={'abc' : 'defga' , 'cde' : 'asdfge','iour' : 'aeiourk' }
print(d)
v=('aeiou')
print(v)
for i,j  in d.items():
    for a in str(i):
        if a in 'aeiou':
            i=i.replace(a,'')
    for b in str(j):
        if b in 'aeiou':
            j=j.replace(b,'')
    e[i]=j

print(e)
