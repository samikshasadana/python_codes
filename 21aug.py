import time;
import calendar
import datetime
localtime = time.localtime(time.time())
print("Local current time :", localtime)
print(time.time())

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)
cal = calendar.month(2018, 1)
print("Here is the calendar:")
print(cal)
time.sleep(10)
c=calendar.month(2018,9)
print(c)
calendar.prcal(2017)
print(calendar.isleap(2020))
print(calendar.firstweekday())
print(calendar.monthcalendar(2018,3))
#time.sleep(10)

t=datetime.date(2018,8,21)
print(t)
w5=t-datetime.timedelta(weeks=5)
print(w5)
w10=t+datetime.timedelta(weeks=10)
print(w10)
print(w5.strftime("%d - %m - %y"))
print(w10.strftime("%d- %m -%y"))
for i in range(12):
    w=t+datetime.timedelta(weeks=3)
    print(w)
    t=w
