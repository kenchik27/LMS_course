from datetime import datetime, date, timedelta
dt_now = datetime.now()
print(dt_now)

dt_1 = datetime(2026, 1, 1, 11, 18, 7, 90000)
print(dt_1)

delta = dt_now - dt_1
print(delta)

dt_3 = delta + dt_1
print(dt_3)


dt = date(2000,1,1)
delta_2 = timedelta(days=1)

dt_4 = dt - delta_2
print(dt_4)

print(dt_now.strftime('%d.%m.%Y %H:%m'))

import locale
locale.setlocale(locale.LC_TIME, "ru_RU")
print(dt_now.strftime('%A %d %B %Y'))

date_string = '12/23/2020'
date_dt = datetime.strptime(date_string, '%m/%d/%Y')
print(date_dt)