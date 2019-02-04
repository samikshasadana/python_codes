from PIL import Image
try:
    i=Image.open('C:\\Users\\RISHABH\\Desktop\\t.jpg')
except IOError:
        pass

w,h=i.size
a=(0,0,w/2,h/2)
r=i.crop(a)
