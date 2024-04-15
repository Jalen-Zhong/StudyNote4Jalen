from celery import Celery
from datetime import timedelta
app = Celery('celery_demo',
     broker='redis://127.0.0.1:6379/2',
     backend='redis://127.0.0.1:6379/1',
     # 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
     include=['test_tasks.task0',
              'test_tasks.task1'
              ])

# 时区
app.conf.timezone = 'Asia/Chengdu'
# 是否使用UTC
app.conf.enable_utc = False