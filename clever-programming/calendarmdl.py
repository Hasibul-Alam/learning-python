import calendar

calendar.setfirstweekday(5)
print(calendar.month(2020,3))
print(calendar.calendar(2020))
print(calendar.weekday(2020,4,11))
print(calendar.isleap(2020))
print(calendar.leapdays(2000,2021))

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2020,4)
print(str)

cale = calendar.Calendar(firstweekday = 5)
for x in cale.iterweekdays():
    print(x)

for x in cale.itermonthdates(2020,4):
    print(x)
pout = cale.itermonthdays(2020,4)
print(pout)
#print(calendar.Calendar())
print(calendar.monthrange(2020,5))
calendar.prmonth(2020,5)
