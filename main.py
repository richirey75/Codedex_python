import datetime
from bday_messages import random_message



today = datetime.date.today()
next_birthday = datetime.date(2025, 5, 6)
days_away = today - next_birthday
print(next_birthday)
if today == next_birthday:
    print(random_message)
else:
    print(f'My next birthday is {days_away.days} days away!')

print(today)