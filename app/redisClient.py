from redis import Redis
from rq import Queue

conn = Redis(host='redis', port=6379)

# create queue
queue = Queue(connection=conn)
