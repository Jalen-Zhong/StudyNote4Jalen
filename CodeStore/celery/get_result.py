from celery.result import AsyncResult
from celery_task import app

async_result = AsyncResult(id = '242c88c6-7993-43c5-9913-89390dbfaa59', app=app)

if async_result.successful():
    result = async_result.get()
    print(result)
