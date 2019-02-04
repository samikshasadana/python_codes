subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            s = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print (s)

n=int(input())
d=int(input())
try:
    n=n/d
    print(n)
    print(a)
except  ZeroDivisionError:
    print('sorry, it is a zero divide error')
except KeyboardInterrupt:
    print('keyboard is pressed')
except NameError:
    print('name is not defined')
except:
    print('bye ji')
else:
    print('hi rishi sir')
finally:
   print('23451')
