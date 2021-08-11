from redis import Redis
from rq import Worker, Queue, Connection

from app.redisClient import conn

listen = ['default']

if __name__ == '__main__':
  with Connection(conn):
    worker = Worker(list(map(Queue, listen)))
    worker.work()
