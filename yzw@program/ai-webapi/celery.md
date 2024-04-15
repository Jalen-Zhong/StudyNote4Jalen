# Celery

## 代码地址：

[StudyNote4Jalen/CodeStore/celery at main · Jalen-Zhong/StudyNote4Jalen (github.com)](https://github.com/Jalen-Zhong/StudyNote4Jalen/tree/main/CodeStore/celery)

## 组件概念：

​	分布式系统，专注于实时处理异步任务，同时支持任务调度。

## 规则流程：

​	User → Broker → Celery Worker → Tasks → Results Store(Backend) → User

## Brocker:

​	Broker在Celery中的主要任务是接收处理任务的指令并将其分发给可用的worker（工作节点）。这个“任务”就好像是一条消息，所以这样的一个中介系统可以被看做是一个消息队列或者是消息代理。Celery支持多种类型的message brokers，例如，RabbitMQ，Redis等。

## Backend:

​	一旦工作节点（worker）完成了任务，它需要将结果存储到某个地方，这就是Celery所说的"backend"。后端的主要任务是存储worker节点处理任务的结果，这样应用程序就可以在之后查询这些结果。Celery可以支持多种类型的backend，包括 AMQP, Redis, memcached, SQLAlchemy (例如PostgreSQL, MySQL)等。

## Celery与Brocker:

​	celery 任务需要连接brocker、创建队列、监听队列、开启并发。

​	而celery组件可以一键部署上述功能，通过`定义异步任务函数`和`启动程序`。

## 程序代码测试：

## 单级目录下的异步任务调度：

### 	创建celery任务并启动：

​		创建celery异步任务，并启动监听

```python
>>celery_task.py:

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


>>cmd:
celery -A celery_task worker -l info


>>output:
 -------------- celery@IT--20240407CZC v5.3.6 (emerald-rush)
--- ***** -----
-- ******* ---- Windows-10-10.0.19041-SP0 2024-04-12 15:25:53
- *** --- * ---
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x242c974a130
- ** ---------- .> transport:   redis://localhost:6379/1
- ** ---------- .> results:     redis://localhost:6379/0
- *** --- * --- .> concurrency: 8 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** -----
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery


[tasks]
  . task.send_email
  . task.send_message

[2024-04-12 15:25:53,404: INFO/MainProcess] Connected to redis://localhost:6379/1
[2024-04-12 15:25:53,409: INFO/MainProcess] mingle: searching for neighbors
[2024-04-12 15:25:53,728: INFO/SpawnPoolWorker-1] child process 2568 calling self.run()
[2024-04-12 15:25:53,738: INFO/SpawnPoolWorker-2] child process 17836 calling self.run()
[2024-04-12 15:25:53,741: INFO/SpawnPoolWorker-3] child process 13852 calling self.run()
[2024-04-12 15:25:53,745: INFO/SpawnPoolWorker-4] child process 7912 calling self.run()
[2024-04-12 15:25:53,761: INFO/SpawnPoolWorker-6] child process 5820 calling self.run()
[2024-04-12 15:25:53,773: INFO/SpawnPoolWorker-5] child process 2388 calling self.run()
[2024-04-12 15:25:53,776: INFO/SpawnPoolWorker-7] child process 17672 calling self.run()
[2024-04-12 15:25:53,780: INFO/SpawnPoolWorker-8] child process 17840 calling self.run()
[2024-04-12 15:25:54,421: INFO/MainProcess] mingle: all alone
[2024-04-12 15:25:54,442: INFO/MainProcess] celery@IT--20240407CZC ready.
```

#### 	问题及解决方式：	

​	①问题：首先是redis拒绝连接，具体报错如下：

```cmd
[2024-04-12 15:33:59,704: ERROR/MainProcess] consumer: Cannot connect to redis://localhost:6379/1: Error 10061 connecting to localhost:6379. 由于目标计算机积极拒绝，
无法连接。..
Trying again in 2.00 seconds... (1/100)
```

​	问题原因：redis未启动。

​	解决方式：首先需要安装配置redis，添加环境变量后执行`redis-server`运行redis，才能执行上述代码。

​	②问题：终端出现如下输出：

```cmd
[2024-04-12 15:25:53,728: INFO/SpawnPoolWorker-1] child process 2568 calling self.run()
```

​	问题原因：该bug可能问题出在window10系统兼容性问题。

​	解决方式：

```cmd
pip install eventlet
celery -A <mymodule> worker -l info -P eventlet
# 参考：https://github.com/celery/celery/issues/4081
```

### 创建用户任务：

​	创建用户任务，目的是调用celery 任务

```python
>>user_task.py:

from celery_task import send_email, send_message

# 调用'send_email'任务函数
result_0 = send_email.delay('temp')
print(result_0.id)

# 调用'send_message'任务函数
result_1 = send_message.delay('temp')
print(result_1.id)


>>output:
    celery_task Terminal:
        [2024-04-12 16:04:17,360: INFO/MainProcess] celery@IT--20240407CZC ready.
        [2024-04-12 16:04:22,656: INFO/MainProcess] Task celery_task.send_email[7e3a25e4-71e1-4b90-903a-		cf06ec62f29c] received
        [2024-04-12 16:04:22,656: WARNING/SpawnPoolWorker-1] Send email to temp...[2024-04-12 16:04:22,656: INFO/MainProcess] Task celery_task.send_message[590cb218-3bcf-4065-93f1-bee334173318] received
        [2024-04-12 16:04:22,656: WARNING/SpawnPoolWorker-2] Send message to temp...
        [2024-04-12 16:04:27,670: WARNING/SpawnPoolWorker-1] Done the task of send email to temp...
        [2024-04-12 16:04:27,670: WARNING/SpawnPoolWorker-2] Done the task of send message to temp...
        [2024-04-12 16:04:27,766: INFO/SpawnPoolWorker-1] Task celery_task.send_email[7e3a25e4-71e1-4b90-903a-cf06ec62f29c] succeeded in 5.125s: 'ok'
        [2024-04-12 16:04:27,766: INFO/SpawnPoolWorker-2] Task celery_task.send_message[590cb218-3bcf-4065-93f1-bee334173318] succeeded in 5.125s: 'ok'
        
    user_task Terminal:
        242c88c6-7993-43c5-9913-89390dbfaa59
        11ba42a9-f983-42c0-84c3-b26ba8f106eb
```

### 	注意：

- 因为是并发任务，`send_email`和`send_message`两个任务是同时执行并输出
- user_task终端打印的为结果id，该id作为任务编号返回给用户，而用户需要用这个id来去`backend`地址查找任务结果，这里两个任务的结果都是`ok`

### 结果查找：

​	根据用户得到的任务编号id，在`backend`地址中查找任务结果

```python
>>get_result.py

from celery.result import AsyncResult
from celery_task import app

async_result = AsyncResult(id = '242c88c6-7993-43c5-9913-89390dbfaa59', app=app)

if async_result.successful():
    result = async_result.get()
    print(result)


>>output；
ok
```

### 	注意:

- 任务成功与否都会返回任务编号id，在通过id查找结果时可能出现一下情况：任务失败、任务仍在执行、任务异常重试、任务等待执行等

## 异步任务调度

```python
from tasks.task01 import send_email
from tasks.task02 import send_msg
from datetime import datetime
v1 = datetime.now()
print(f"当前时间:{v1}")
# 立即告知celery去执行test_celery任务，并传入一个参数
#result = send_email.apply_async(('yuan',),queue="testq")
result = send_email.delay('yuan')
print(f"任务ID:{result.id}")
result = send_msg.delay('yuan')
print(f"任务ID:{result.id}")
```

## 定时任务

### celery队列定义：

```python
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
```

### 定时任务调度方式：

```python
from tasks.task01 import send_email
from tasks.task02 import send_msg
from datetime import datetime
#方式一 固定时间
print('--------Method 0--------:')
v1 = datetime(2022, 4, 15, 14, 20, 00)
print(f"当前时间:{v1}")
v2 = datetime.fromtimestamp(v1.timestamp())
print(f"任务运行时间:{v2}")
result = send_email.apply_async(args=["定时任务-指定时间"], eta=v2)
print(f"任务ID:{result.id}")

# 方式二
print('--------Method 1--------:')
ctime = datetime.now()
print(f"当前时间:{ctime}")
utc_ctime = datetime.fromtimestamp(ctime.timestamp())
from datetime import timedelta
time_delay = timedelta(seconds=30)
task_time = utc_ctime + time_delay
print(f"任务运行时间:{task_time}")
#使用apply_async并设定时间
result = send_msg.apply_async(args=["定时任务-延时10秒"], eta=task_time)
print(f"任务ID:{result.id}")
```

## 周期任务：

### celery周期任务定义：

```python
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
```

### 周期任务调度：

celery启动命令：`celery -A [tasks] beat -l info`

### 其他：

上述周期任务执行时，回每10s插入一份任务，但不执行，当启动`worker`时，会执行所插入任务。另外，即使当`beat`关闭时，也会执行先前所插入任务，这叫执行历史遗留任务。

### 查询历史遗留任务：

#### 方法一：

cmd → `redis-cli` → select [dp] (broker) → `keys *` → `type celery` → `lrange celery 0 -1`

#### 方法二：

```python
celery_cache_task_check.py

import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=2)

for i in r.lrange('celery', 0, -1):
    print(i)
```

### 启动自定义worker对celery队列任务的并发处理数量

`celery -A [tasks] worker -l info -c [num]`

### 清空历史遗留任务

```python
celery_cache_task_check.py

import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=2)
# 删除任务缓存
r.delect('celery')

for i in r.lrange('celery', 0, -1):
    print(i)
```

# celery组件学习笔记

## 目录架构：

```
celery:
	| README.md
	| .gitignore
	|
	|—— celery02:定时任务与周期任务
	|—— sinple_structure_task:单目录的异步任务
	|—— 单目录定时任务
		
```

