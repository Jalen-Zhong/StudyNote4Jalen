from celery_task import send_email, send_message

# 调用'send_email'任务函数
result_0 = send_email.delay('temp')
print(result_0.id)

# 调用'send_message'任务函数
result_1 = send_message.delay('temp')
print(result_1.id)
