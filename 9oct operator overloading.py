#1
'''class complex:
    def __init__(self):
        self.real=0
        self.img=0
    def setval(self,r,i):
        self.real=r
        self.img=i
    def __add__(self,c):
        temp=complex()
        temp.real=self.real+c.real
        temp.img=self.img+c.img
        return temp
    def __sub__(self,c):
        temp=complex()
        temp.real=self.real-c.real
        temp.img=self.img-c.img
        return temp
    def disp(self):
        print(self.real,self.img,'i')

c=complex()
c.setval(1,2)
c1=complex()
c1.setval(3,4)
c2=complex()
c2=c+c1
c3=complex()
c3=c-c1
c2.disp()
c3.disp()


#2
class stu:
    def __init__(self,n,m):
        self.n=n
        self.m=m
    def disp(self):
        print(self.n,self.m)
    def __add__(self,c):
        temp=stu(self.n,[])
        for i in range(len(self.m)):
            temp.m.append(self.m[i]+c.m[i])
       # print(temp.m)
        return temp
        
c=stu('rishi',[1,2,3])
c.disp()
c1=stu('rishi',[3,4,5])
c2=stu("",[])
c2=c+c1
c2.disp()
'''

#3
class b:
    def __init__(self,m):
        self.m=m
    def disp(self):
        print(self.m)
    def __gt__(self,b):
        if self.m>b.m:
            print(self.m)
            return True
        else:
            print(b.m)
            return False
        
n=b(123)
ax=b(1234)
if n>ax:
    print('hi')
else:
    print('bye')
    

