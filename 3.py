a=int(input("enter no."))
h=hex(a)
o=oct(a)
s=a**0.5
print(h,o,s)
sp=int(input("enter sports marks"))
a1=int(input("enter a1 marks"))
a2=int(input("enter a2 marks"))
a3=int(input("enter a3 marks"))
ex=int(input("enter exam marks"))
res=0.2*sp+0.3*a1+0.3*a2+0.3*a3+0.5*ex
print("your result is",res)
tec=int(input("enter no. of tens coin"))
fc=int(input("enter no. five coin"))
twc=int(input("enter no. two coin"))
oc=int(input("enter no. one coin"))
total=10*tec+5*fc+twc*2+oc*1
print("your total money is",total)
s=(input("enter string"))
print("%.6s"%s)
