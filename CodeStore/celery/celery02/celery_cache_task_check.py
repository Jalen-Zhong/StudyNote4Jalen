import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=2)
# r.delete('celery02')

for i in r.lrange('celery02', 0, -1):
    print(i)