'''def changeme():
    num=int(input())
    listWithDuplicates=[]
    for i in range(num):
        ele=int(input())
        listWithDuplicates.append(ele)
        removeDup(listWithDuplicates)

def removeDup(lst):
    if len(lst)== 0:
        print("List is empty")
    else:
        newList=[]
        for i in lst:
            if i in newList:
                pass
            else:
                newList.append(i)
                print(list(newList))

changeme()
'''
'''
#2
def rev(s1):
    num=s1
    s2=0
    while(num!=0):
        rem=num%10
        s2=s2*10+rem
        num=num//10
    if(s1==s2):
        return True
    else:
         return False
        
str=int(input())
num=str
if(rev(str)):
    sum=0
    while(num!=0):
        rem=num%10
        sum=sum+rem
        num=num//10
    print("since no. was palindrome therefore sum of digits =",sum)
else:
    count=0
    while(num!=0):
        count+=1
        num=num//10
    print("no. is not palindrome thus total no. of digits = ",count)
'''
#3
text=input()
total = 0
lower = text.lower()
most = lower[0]
for i in lower:
        if i.isalpha():
                if lower.count(i) > total:
                        most = i
                        total = lower.count(i)
                elif lower.count(i) == total:
                        if i < most:
                                most = i

                                total = lower.count(i)
print (most)

