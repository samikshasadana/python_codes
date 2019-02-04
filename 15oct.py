class DissCheck(object):
    def findCheck(self, nums):
         '''for i in range(len(nums)):
                      index = abs(nums[i]) - 1
                      nums[index] = - abs(nums[index])
            return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
         return list(set(range(1, len(nums) + 1)) - set(nums))
    def main():
        l=[]
        n = int(input())
        for i in range(n):
            l.append(int(input()))
            s = DissCheck()
            ans=s.findCheck(l)
            print(ans)
    main()
'''
from tkinter import *
#Tk,Label,Button
from PIL import ImageTk,Image
t=Tk()
#w=t.Tk()
t.geometry('700x720+450+650')
msg=Label(t,text='hi rishi',background='green')
t.configure(background='yellow')
p=("C:\\Users\\RISHABH\\Desktop\\t.jpg")
msg.pack(side='left')
i=ImageTk.PhotoImage(Image.open(p))
p=Label(t,image=i)
p.pack(side = 'bottom',expand='yes')
t.title('rishi')
w=t.winfo_screenwidth()
print(w)
print(t.winfo_screenheight())
b=Button(t,text='exit1',command=t.destroy)
b.pack()
def call():
    print('hi')
b2=Button(t,text='bye1',command=call)
b2.pack()
#t.attributes('-fullscreen',True)
a=Entry(t,bd=5)
a.pack()
print(a)

t.mainloop()


