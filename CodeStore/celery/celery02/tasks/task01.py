import time
from tasks.celery import app
#这是关键，穿上这件衣服就是异步任务函数了
@app.task
def send_email(res):
    print("开始向%s发送邮件任务"%res)
    time.sleep(5)
    print("完成向%s发送邮件任务"%res)
    return "mail ok"