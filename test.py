import redis
import os

def test_redis_basic():
    redis_url = os.environ['REDISTOGO_URL']
    print(f'Redis Connection url from env_var: {redis_url}')
    redis_conn = redis.from_url(redis_url)

    # set value for a key
    redis_conn.set('test_basic', 123)

    # retrieve value
    retrieved_val = redis_conn.get('test_basic')
    print(f'Retrieved value: {retrieved_val}')

   # redis://redis:6379