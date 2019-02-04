import re
string="i am an indian"
pattern="am"
if re.match(pattern,string):
    print("match found")
else:
    print("not found")



'''
pattern="am"
if re.search(pattern,string):
    print("match found")
else:
    print("not found")




string="hidededede"
pattern="hi(de)+"
if re.match(pattern,string):
    print("match found")
else:
    print("not found")




string=input()
pattern="[0-9]+[a-z A-Z]+|[a-z A-Z]+[0-9]+"
if re.match(pattern,string):
    print("match found")
else:
    print("not found")



pattern="[a-z]+ \d+"
string="lxi 2014,abc 2016"
m=re.findall(pattern,string)
for n in m:
    print(n)




string="i am an indian"
pattern=r"\b\w\w"
m=re.findall(pattern,string)
for n in m:
    print(n)



string="date is 4-9-2017"
pattern="[0-9]+\W[0-9]+\W[0-9]+"
m=re.findall(pattern,string)
for n in m:
    print(n)'''


string="i am a girl"
pattern=r"\b[aeiouAEIOU]+\w*"
m=re.findall(pattern,string)
for n in m:
    print(n)




string="724473 7996543210 5123467890"
pattern=r"\b[789]{1}[0-9]{9}"
m=re.findall(pattern,string)
for n in m:
    print(n)


string=input()
pattern='ab*'
if re.match(pattern,string):
    print("match found")
else:
    print("not found")
