import time
from tasks.celery import app
@app.task
def send_msg(name):
    print("开始向%s发送短信任务"%name)
    time.sleep(5)
    print("完成向%s发送短信任务"%name)
    return "msg ok"