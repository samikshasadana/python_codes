'''f=open("rk.txt",'w')
f.write("hi rishi \n")
print('\n')
f=open("rk.txt",'a')
f.write(" by rishi for you \n" )
f=open("rk.txt",'r')
print(f.read())
f=open("rk.txt",'r')
print(f.read(5))
print(f.readline())
f=open("rk.txt",'a')
f.write(" by rishi for you agin \n at your service \n" )'''
f=open("rk.txt",'r')
print(f.read(10))
print(f.seek(3,2))
print(f.read(5))


