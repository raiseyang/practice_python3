redis官网:https://redis.io/

redis-py创库地址:https://github.com/andymccurdy/redis-py

```
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0,
                            # password='adups2017'
                            )
r = redis.Redis(connection_pool=pool)

r.set('foo','bar')

print(r.get('foo'))
```