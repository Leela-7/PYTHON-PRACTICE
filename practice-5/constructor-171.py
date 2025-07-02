class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

time1 = Time(11, 45, 30)
time2 = Time(12, 45, 40)

print(time1.hour, time1.minute, time1.second)
print(time2.hour, time2.minute, time2.second)
