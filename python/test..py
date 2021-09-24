from datetime import datetime, timedelta

yesterday = datetime.today() - timedelta(1)

print(yesterday)

year = yesterday.year
month = yesterday.month
day = yesterday.day

print(year)
print(month)
print(day)