s=float(input("enter salary"))
g=(input("enter gender"))
if(s<10000)&(g=='m'):
  s=0.07*s+s 
  print("your final salary is %f"%s)
elif(s>=10000)&(g=='m'):
   s=0.05*s+s 
   print("your final salary is %f"%s)
elif(s<10000)&(g=='f'):
   s=0.12*s+s 
   print("your final salary is %f"%s)
elif(s>10000)&(g=='f'):
    s=0.1*s+s 
    print("your final salary is %f"%s)


s=input("enter character")
if(s=="a" or s=='e'or s=='i'or s=='o'or s=='u' or s=="A" or s=="E" or s=="I" or s=="O" or s=="U" ):
    print("entered character is vowel")
else:
    print("not vowel sir/mam ")
print("ascii value is", ord(s))

a=input("enter str1")
b=input("enter str2")
if(a is b):
    print("same location")
else:
    print("not same location of memory")
print(id(a),id(b))


    
