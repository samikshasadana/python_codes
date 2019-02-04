'''class base:
    def show(self):
        print('hi')
    def disp(self):
        print('bye in base sir!')

class der(base):
    def disp1(self):
        print('hi rishi in derive1')
    a=21
class der2(der):
    def disp2(self):
        print('in derived 2')
    b=3

class der3(der,der2):
    def disp3(a,b):
        print(a,b)
        

o=der3()
o.disp()
o.disp1()
o.disp2()
o.disp3()'''

class base1:
    def __init__(self):
        self.a=4
    def show(self):
        print('hi')
    def disp(self):
        print('bye in base sir!')


class base2:
     def __init__(self):
        self.b=9
     def disp1(self):
        print('hi rishi in derive1')
    
class der(base1,base2):
    def disp2(self):
        print('in derived 2')
    def disp3(self):
        print(self.a)
o=der()
o.disp()
o.disp1()
o.disp2()
o.disp3()
