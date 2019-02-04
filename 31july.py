'''n=int(input("enter no. of elements"))
a=[]
for i in range(n):
    e=int(input("enter element"))
    a.append(e)
a.sort()
a.reverse()
l=len(a)
for i in range(l):
    if a[i]>a[i+1]:
        print("second largest: ",a[i+1])
        break;


n1=int(input("enter n1 capacity"))
n2=int(input("enter n2 capacity"))
n3=int(input("enter n3 capacity"))
n4=int(input("enter n4 capacity"))
nt=int(input("enter total cars"))
s=nt-n1
if(s<=0):
    print("B1")
elif(s-n2<=0):
    print('B2')
elif(s-n2-n3<=0):
    print('B3')
elif(s-n2-n3-n4<=0):
    print('B4')
else:
    print('EXT')'''


s=int(input("enter no. of names"))
l=[]
fn=[]
for i in range(s):
    x=(input("enter name"))
    l.append(x)
for j in range(len(l)):
    fn=l[j].split(" ")
    if len(fn)==1:
        b=fn[0]
        e=b[1:len(b)]
        print(b[0].upper()+e.lower())
    elif len(fn)==3:
        b=fn[0]
        c=fn[1]
        d=fn[2]
        e=d[1:len(d)]
        print(b[0].upper()+"."+c[0].upper()+"."+d[0].upper()+e.lower())
    elif len(fn)==2:
        c=fn[0]
        d=fn[1]
        e=d[1:len(d)]
        print(c[0].upper()+"."+d[0].upper()+e.lower())
    else:
        print("error")
'''
a=input("enter no. of names")

 

names=[]

final_name=[]

for i in range(0,int(a)):

    n=input()

    names.append(n)

 

for j in range(0,len(names)):

    final_name=names[j].split(" ")

    if len(final_name) == 1:

        b = final_name[0]

        e= b[1:len(b)]

        print(b[0].upper() + e.lower())

    elif len(final_name) == 3:

        b = final_name[0]

        c = final_name[1]

        d = final_name[2]

        e = d[1:len(d)]

        print(b[0].upper() + ". " + c[0].upper() + ". " + d[0].upper() + e.lower())

    elif len(final_name) == 2:

        c = final_name[0]

        d = final_name[1]

        e = d[1:len(d)]

        print(c[0].upper() + ". " + d[0].upper() + e.lower())

    else:

        print("Error")'''

        





