'''try:
    f=open("rk.txt",'w')
    f.write("hi rishi")
    #print('\n')
    f=open("rk.txt",'a')
    f.write(" by rishi for you \n" )
    f=open("rk.txt",'r')
    print(f.read())
    l=f.split('  ')
    print(l)
except:
    print('hi sir')

'''
'''
f=open("rk.txt",'r')
print(f.read(5))
print(f.readline())
f=open("rk.txt",'a')
f.write(" by rishi for you agin \n at your service \n" )
'''
f=open("rk.txt",'w')
f.write("hi rishi")
    #print('\n')
f=open("rk.txt",'a')
f.write(" by rishi for you \n" )
f=open("rk.txt",'r')
#print(f.readline())
d=f.read()
k=d.split(' ')
print(k)
