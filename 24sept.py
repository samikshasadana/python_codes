import re
'''s=input()
p=' /?.!@#$%^&*() '
if re.search(p,s):
    print(' not found ')
else:
    print(' found')

#2
s=input()
p=r'\w+[ab]+\w'
if re.search(p,s):
    print(' match found ')
else:
    print(' not found')

#3

s=input()
p='exercise'
c=0
x=re.findall(p,s)
for i in x:
    c=c+1
print(c)
l='rishi'
print(re.sub(p,l,s))

#4
s=['bush','fox','toy','cap','candy']
l=[]
for i in s:
    if i.endswith('h',0,len(i)):
        i=i+'es'
        l.append(i)
    elif i.endswith('x',0,len(i)):
        i=i+'es'
        l.append(i)
    else:
        i=i+'s'
        l.append(i)
print(l)
'''
#5
rk=[]
s=['bush','fox','toy','cap','candy']
p1='[^aeiou][hxp]$'
p2='[^aeiou]y$'
for i in s:
    if re.search(p1,i):
       rk.append(i+'es')
    elif re.search(p2,i):
        rk.append(i[:len(i)-1]+'ies')
    else :
        rk.append(i+'s')
print(rk)
'''
#6
s=input()
l=[]
p1='cats'
p2='dogs'
c=0
x=re.findall(p1,s)
y=re.findall(p2,s)
for i in x:
    c=c+1
print('cats',c)
c=0
for i in y:
    c=c+1
print('dogs',c)
p3='[0-9]+'
print(re.findall(p3,s))
'''
#7
s=input()
p1=r'[a-z]'
p2=r'[A-Z]'
p3=r'[ 0-9 ]'
p4=r'[@!#$&] '
l=len(s)
if (re.search(p1,s)) and (re.search(p2,s)) and (re.search(p3,s)) and (re.search(p4,s)) and (l>6) and (l<=12):
        print('valid')
else:
        print('not valid')
