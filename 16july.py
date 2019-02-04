t="master rishi you are very great and genious please be positive "
print(t)
i=1
sum=0
n=float(input("enter term upto which u want to print sum"))
while(i<=n):
    sum=i/(i+1)+sum
    i=i+1
print("sum of series 1/2+2/3+3/4... is%f",sum)

n=float(input("enter no."))
if(n%3==0)&(n%5==0):
    print("fizz buzz")
elif(n%3==0):
    print("fizz")
elif(n%5==0):
    print("buzz")
else:
    print("not divisible by both")
    
i=1500
while(i<=2700):
    if(i%7==0):
        print(i,end=" ")
    i=i+1
