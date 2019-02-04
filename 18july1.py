
def s_return(num):
    return num**2

def s_print(b):
    print(b**2)
    
n=10
print("global variable",n)
def fun(a):
    print("in local",a)
    b=30
    print(b)

    
fun(20)
print(n)
print(b)
