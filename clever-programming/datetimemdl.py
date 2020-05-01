import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(1993,6,26)
print(birthday)

days_since_birth = (today - birthday).days
print(days_since_birth)

tdelta = datetime.timedelta(days = 10)
print(today + tdelta)

tback = datetime.timedelta(days = 10)
print(today - tback)

print(today.day)
print(today.weekday())

print(datetime.time(10, 31, 32, 16))
# datetime.date(Y, M, D)
# datetime.time(h, m, s, ms)
# datetime.datetime(Y, M, D, h, m, s, ms)

print(datetime.datetime.now())
# Add 10 hours to current time
hour_delta = datetime.timedelta(hours = 16)
print(datetime.datetime.now() + hour_delta)

datetime_today = datetime.datetime.now(tz = pytz.UTC)
datetime_dhaka = datetime_today.astimezone(pytz.timezone('Asia/Dhaka'))
print(datetime_dhaka)
for tz in pytz.all_timezones:
    print(tz)
