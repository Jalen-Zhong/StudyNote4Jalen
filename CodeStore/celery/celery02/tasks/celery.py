from celery import Celery
from datetime import timedelta

app = Celery('celery_demo',
     broker='redis://127.0.0.1:6379/2',
     backend='redis://127.0.0.1:6379/1',
     # 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
     include=['tasks.task01',
              'tasks.task02'
              ])

app.conf.timezone = 'Asia/Shanghai' # 时区
app.conf.enable_utc = False # 是否使用UTC
app.conf.task_default_queue = "celery02"  #修改默认队列,可以不要
#配置文件定时任务
app.conf.beat_schedule = {
    'sendmail-every-10-seconds': {
        # 定义执行任务
        'task': 'tasks.task01.send_email',
        # 'schedule' : 1.0 # 表示1s执行一次
        # # 'schedule' : crontab(minute='*/1') # 表示1 min 执行一次
        'schedule': timedelta(seconds=10),
        # send email相关传入参数
        'args': ('李四',)
    },
}