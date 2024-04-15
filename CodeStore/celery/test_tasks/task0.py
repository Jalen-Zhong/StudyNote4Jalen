import time 
from test_tasks.celery import app

@app.task
def send_email(name):
    print('Send email to %s...' % name)
    time.sleep(5)
    print('Done the task of send email to %s...' % name)
    return 'email task......'