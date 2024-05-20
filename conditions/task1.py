from datetime import date, time, datetime, timedelta

birth_date = datetime(2000, 11, 9)
now = datetime.now()
age_year = now.date() - birth_date.date()
age = now - birth_date
print(age)
