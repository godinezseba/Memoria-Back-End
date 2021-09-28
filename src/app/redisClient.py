from redis import Redis, from_url
from rq import Queue
from os import environ

conn = from_url(environ.get('REDIS_URL'))
# conn = Redis(
#     host=environ.get('REDIS_HOST'),
#     port=environ.get('REDIS_PORT'),
#     db=environ.get('REDIS_DB'),
#     password=environ.get('REDIS_PASS'),
#     username=environ.get('REDIS_USER'),
#     client_name=environ.get('REDIS_USER'),
# )

# create queue
queue = Queue(connection=conn)
