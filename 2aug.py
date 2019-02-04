s=(input("enter string"))
t=(input("enter sub string"))
l=[]
count=0
l=t.split()
s=s.split()
for i in range(len(l)):
    for j in range(len(s)):
        if(t[i] in s[j]):
            count=count+1
            print(s.index(l[i]))
print(count)
        

'''n=int(input("enter no."))
for i in range(n+1):
    for j in range(n-1):
        print('#',end="")
        print('*')'''

n=int(input("enter no."))
a=[]
for i in range(n):
    s=(input("enter string"))
    a.append(s)
    
    
    
