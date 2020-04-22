from datetime import datetime, date, time, timedelta

# 1.自定义日期和时间
d = datetime(2020, 10, 30, 14, 5)
print(d)

d2 = date(2019, 3, 23)
print(d2)

t = time(9, 0)
print(t)

print('--------------------')
# 2. 日期、时间与字符串之间的相互转换
# 字符串转换datetime对象
ds = '2018/10/3T13:42:09'
ds_t = datetime.strptime(ds, '%Y/%m/%dT%H:%M:%S')
print(ds_t.second)
# datetime对象转换成字符串
print('--------------')
n = datetime.now()
print(n)
n_str = n.strftime('%m')
print(n_str)


# 3. datetime之间的加减操作
print('-------------')
n = datetime.now()
print(n)
n_next = n + timedelta(days=5, hours=42, minutes=4, seconds=56, microseconds=444)
print(n_next)

print('---------------')
# 时间的减法
d1 = datetime(2018, 10, 15)
d2 = datetime(2018, 11, 12)

rest = d2 - d1
print(type(rest))
print(rest.days)

rest2 = d1 - d2
print(rest2.days)
