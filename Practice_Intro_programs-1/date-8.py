from datetime import datetime
today=datetime.now()
days=["mon","tues","wednes","thurs","fri","satur","sun"]
print(today)
print(today.day)
print(today.month)
print(today.weekday())
print(days[today.weekday()])



