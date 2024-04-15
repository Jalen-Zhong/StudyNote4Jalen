from tasks.task01 import send_email
from tasks.task02 import send_msg
from datetime import datetime
v1 = datetime.now()
print(f"当前时间:{v1}")
# 立即告知celery去执行test_celery任务，并传入一个参数
#result = send_email.apply_async(('yuan',),queue="testq")
result = send_email.delay('yuan')
print(f"任务ID:{result.id}")
result = send_msg.delay('yuan')
print(f"任务ID:{result.id}")