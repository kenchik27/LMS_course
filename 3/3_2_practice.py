
# напечатайте даты: вчера сегодня 30 дн назад
from datetime import datetime,timedelta
dt_now = (datetime.now()).date()
time_delta = timedelta(days=1)
dt_yesterday = dt_now - time_delta
delta_2 = timedelta(days=30)
dt_30_ago = dt_now - delta_2

print(dt_now)
print(dt_yesterday)
print(dt_30_ago)

# превратите строку "01/01/25 12:10:04.234567"
# в объект datetime
string = "01/01/25 12:10:04.234567"
date_ = datetime.strptime(string, '%d/%m/%y %H:%M:%S.%f')
print(date_)