from tasks.task01 import send_email
from tasks.task02 import send_msg
from datetime import datetime
# #方式一 固定时间
print('--------Method 0--------:')
v1 = datetime(2024, 4, 15, 15, 37, 00)
print(f"当前时间:{v1}")
v2 = datetime.utcfromtimestamp(v1.timestamp())
print(f"任务运行时间:{v2}")
result = send_email.apply_async(args=["定时任务-指定时间"], eta=v2)
print(f"任务ID:{result.id}")

# 方式二
print('--------Method 1--------:')
ctime = datetime.now()
print(f"当前时间:{ctime}")
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
from datetime import timedelta
time_delay = timedelta(seconds=10)
task_time = utc_ctime + time_delay
print(f"任务运行时间:{task_time}")
#使用apply_async并设定时间
result = send_msg.apply_async(args=["定时任务-延时10秒"], eta=task_time)
print(f"任务ID:{result.id}")