from datetime import datetime
import time

now_time = datetime.now()

print("now: {0}".format(now_time))

# 当前的日期
print('now day: {0}'.format(now_time.date()))

# 当前的时间
print('now time: {0}'.format(now_time.time()))

print('now day2: {0}'.format(datetime.today()))

print('year: {0}'.format(now_time.year))
print('month: {0}'.format(now_time.month))
print('day: {0}'.format(now_time.day))
print('microsecond: {0}'.format(now_time.microsecond))

print(dir(now_time))

print('------------------')
# 获取到毫秒数
print(time.time())
#
time.sleep(2)
