class human:
    def say(self,name='none'):
        if name is not 'none':
            print('hello '+name)
        else:
            print('hello')
a=human()
a.say()
a.say('rishi')

def add(d,*args):
        if d=='int':
            an=0
            ab=1
            for x in args:
                an=an+x
                ab=ab*x
            print(an,ab)
        if d=='str':
            an=' '
            for x in args:
                an=an+x
            print(an)

add('int',5,6,7)
add('str','hello','rishi')

class stu:
    def __init__(self,List):
        self.List=List
    def disp(self):
        print(self.List)
    def __add__(self,M):
        temp=stu([])
        for i in range(len(self.List)):
            for j in range(len(self.List[0])):
                temp.List.append(self.List[i][j]+M.List[i][j])
        return temp
a=stu([[1,2],[3,4]])
a.disp()
b=stu([[3,4],[5,1]])
b.disp()
c=stu([])
c=a+b
c.disp()


