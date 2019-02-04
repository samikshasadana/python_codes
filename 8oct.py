
'''class abc:
    def __init__(self,v,v1,v2):
        self.v=v
        self.__v1=v1
        self._v2=v2
    def disp(self):
        print(self.v)
        print(self.__v1)
        print(self._v2)

o=abc(3,5,2)
print(o.v)
#print(o._v1)
print(o._abc__v1)
print(o._v2)
o.disp()
'''
#2
import re
class str:
    def upper(self,s):
        self.c=0
        self.c1=0
        self.c3=0
        self.c2=0
        for i in range(len(s)):
            if s[i].isupper():
                self.c=self.c+1
            elif s[i].islower():
                self.c1+=1
            elif s[i].isdigit():
                self.c3=self.c3+1
            elif s[i]==' ':
                self.c2+=1
                
        print("total uppercases are",self.c)
        print("total lowercases are",self.c1)
        print("total digits are",self.c3)
        print("total spaces are",self.c2)
s=input()
o=str()
o.upper(s)

