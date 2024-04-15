from celery.result import AsyncResult
from tasks.celery import app

print('Please input task id for query task result:')
id = input()
print('Result display:')
async_result = AsyncResult(id = id, app=app)

if async_result.successful():
    result = async_result.get()
    print(result)
