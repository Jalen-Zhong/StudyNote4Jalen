from celery import Celery
import time
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

# 定义后端存储地址
backend = 'redis://localhost:6379/0'
# 定义代理地址
broker = 'redis://localhost:6379/1'

# celery作为一个单独项目运行，在settings文件中设置
broker_connection_retry_on_startup = True

# 创建celery对象
app = Celery('tasks', backend=backend, broker=broker, broker_connection_retry_on_startup = True)

# 定义异步函数任务
@app.task
def send_email(name):
    print('Send email to %s...' % name)
    time.sleep(5)
    print('Done the task of send email to %s...' % name)
    return 'ok'

# 定义异步函数任务
@app.task
def send_message(name):
    print('Send message to %s...' % name)
    time.sleep(5)
    print('Done the task of send message to %s...' % name)
    return 'ok'