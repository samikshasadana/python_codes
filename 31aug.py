
'''A = [[12, 7, 3],     [4, 5, 6],     [7, 8, 9]]
B = [[5, 8, 1, 2],     [6, 7, 3, 0],     [4, 5, 9, 1]]
re= [[0, 0, 0, 0],         [0, 0, 0, 0],         [0, 0, 0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            re[i][j] += A[i][k] * B[k][j]
for r in re:
        print(r)
        '''
  
#2
matrix=[[0,0,0,1,0],[2,0,0,0,3],[0,0,0,4,0]] 
Dict={}
for i in range(len(matrix)):
    print(" ")
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
        if matrix[i][j]!=0:
            Dict[(i,j)]= matrix[i][j]
print(' \n Sparse Matrix Representation on Dictionary')
print(Dict)

#3
import re
a="scream,you scream,we all scream for ice cream"
j=[m.start() for m in re.finditer('scream',a)]
print(j)
#4
'''
import math
size = int(input("enter size  "))
arr = list()
for i in range (0,size):
    temp = input("enter no.")
    arr.append(temp)
arr.sort()
search = int(input('enter no. to be search'))
int(search)
half = int(size/2)
math.floor(half)
if search <= int(arr[half]):
    for i in range(half,0,-1):
        if(search == int(arr[i])):
            print('index of element is {}'.format(i+1))
            break
        else:
            print("Number not Found")
            break
else:
    for i in range(half,size,1):
        if(search == int(arr[i])):
            print('index of element is {}'.format(i+half-1))
            break
        else:
            print("Number not Found")
            break
'''
#6

a = "i scream, you scream, we all scream for ice cream"
print(a)
print(a.capitalize())
print(a.find("scream",a.find("scream")+len("scream")))
print(a.center(len(a)+6,"*"))
print(len(a))
print(a.replace("scream","love",a.count("scream")))
print(a  + " Lets Eat it")
#7
'''

acno = input('Enter A/C no')
b=2500000000
service = input('Enter 1 for Balance \nEnter 2 for Mini Statement\nEnter 3 for Last Transaction\n')
if service=='1':
    print('Balance : ')
    print(b)

elif service=='2':
    print('Mini Statement')
    print('sir/mam you are valueable for us please keep growing!!')

elif service=='3':
    print('Last Transaction')
    print('you didnt did any transaction yet!!,wanna do?')
    x= input()
    if(x=='Y') or x=='y':
        c=int(input('enter amount to withdraw '))
        b=b-c
        print('new balance is :-', b)

else:
    print('Please Enter a Valid Option')
    '''
#8

a=[1,2,3,4]
b=[4,5,6,7]
c=0;
while c!=4:
    print("1 : add ")
    print("2 : subtract ")
    print("3 : multiply")
    print("4 : exit")
    c=eval(input("Enter choice : "))
    x=-1;
    print(a," ",b)
    if c==1:
        for i in a:
            x+=1;
            for v in b[x:x+1]:
                d=i+v;
                print(d);
    if c==2:
        for i in a:
            x+=1;
            for v in b[x:x+1]:
                d=i-v;
                print(d);
    if c==3:
        for i in a:
            x+=1;
            for v in b[x:x+1]:
                d=i*v;
                print(d);
#9
dic={'abc':'cde','iab':'oab','eeb':'zxu'}
d={x:y for x,y in dic.items() if x not in 'aieou' and y not in 'aeiou' }
print(d)
