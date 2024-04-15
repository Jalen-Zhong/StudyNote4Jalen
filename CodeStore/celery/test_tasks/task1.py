import time 
from test_tasks.celery import app

@app.task
def send_message(name):
    print('Send message to %s...' % name)
    time.sleep(5)
    print('Done the task of send message to %s...' % name)
    return 'messege task......'