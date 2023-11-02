import datetime

# 获取当前日期
current_date = datetime.date.today()
print("当前日期:", current_date)

# 获取指定日期
specified_date = datetime.date(2023, 11, 2)
print("指定日期:", specified_date)

# 获取当前时间
current_time = datetime.datetime.now().time()
print("当前时间:", current_time)

# 获取当前日期和时间
current_datetime = datetime.datetime.now()
print("当前日期和时间:", current_datetime)

delta = datetime.timedelta(days=1)
print(delta)