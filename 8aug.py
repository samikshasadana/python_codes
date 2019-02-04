rk = {'rishi': [80,90,80],'rajat':[80,90,90],'ramya':[80,90,80]}
s=0
x=0
l=sorted(rk.values())
d={}
print(l[-1])
for i,j in rk.items():
    t=sum(j)
    rk[i]=t
print(rk)
l=sorted(rk.values())
x=l[-1]
print(x)
for i,j in rk.items():
    if(j>=x):
        x=j
        d[i]=x
print(d)
    

l=[1,2,3,4,5,6]
k=[0,9,8,7,6]
print(dict(zip(l,k)))
k='uouimUYHIopi'
print(k.swapcase())

d={'bud':'dost','donkey':'gadha'}
e={'dost':'mitr','gadha':'donkey'}
print('Sir rishi you are genious....!!!!')
for i in d:
    print(i,'in hindi means',d[i])
    print(' in punjabi it means ',e[d[i]])



    
