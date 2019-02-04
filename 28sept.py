import re

s=input()
#p=r'\b[a-z A-z 0-9  \W ]+@[a-z A-z ]+.[a-z A-Z]\b)'
p=r'[\w.-]+@[\w.-]+'
p1=r'@[\w.-]+\b'
p2=r'[\w.-]+@'
x=re.findall(p,s)
print(x)
y=re.findall(p1,s)
print(y)
z=re.findall(p2,s)
for i in z:
    print(i[:-1])

#2
s=input()
avg=0
c=0
k='done'
p='[a-z A-Z]'
while s is not k:
    if (re.findall(k,s)):
        break
    elif s in p:
        print('sir ji... number please')
        s=input()
    else:
        c=c+1
        avg=int(s)+avg
        s=input()

print('count= ',c,'   avg= ',avg/c)
