import math
a=math.sinh(90)
print(a)


import random
b = random.randint(1,100)
print(b)


from datetime import datetime, timedelta
now = datetime.now()
print(now.year)
print(now)
print(now.month)
f = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted:", f)


timestamp = now.timestamp()
print("TS:",timestamp)


future = now + timedelta (days=7)
past = now + timedelta (days=5)


print(future)
print(past)


