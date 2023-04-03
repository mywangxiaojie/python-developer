import json
import subprocess
import sys
from time import sleep
import multiprocessing
import time
import logging

import redis
from celery import Celery, current_task

logger = logging.getLogger(__name__)

redis_host = f"redis://:admin@127.0.0.1:6379/0"

celery = Celery(__name__)
celery.config_from_object({
    'timezone': 'Asia/Shanghai',
    'enable_utc': False,
    'broker_url': redis_host,
    'result_backend': redis_host,
    'worker_pool_restarts': True,  # Required for /worker/pool/restart API
    'task_reject_on_worker_lost': True,  # worker意外终端，任务放回队列
    'task_acks_late': False,  # 任务完成才从队列中删除
    'worker_max_tasks_per_child': 100,  # 每个worker最多执行完100个任务就会被销毁，可防止内存泄露
    'worker_concurrency': 20,  # worker最大并发数
    'worker_prefetch_multiplier': 1,
    'task_track_started': True,
    'task_ignore_result': False,
    'task_store_errors_even_if_ignored': True,
    'celeryd_force_execv': True,
    'worker_send_task_events': True,
    'task_send_sent_event': True,
    'broker_transport_options': {'visibility_timeout': 1800}
})


# arcface_detector.reg_arcface()
# face_info.load_person_infos()

@celery.task
def add(x, y):
    while True:
        sleep(3)
        print(x + y)
        print(current_task.request)
        print(current_task.request.id)

@celery.task
def sub(x, y):
    sleep(30)  # Simulate work
    return x - y

def test_monitor(app):
    state = app.events.State()

    def announce_failed_tasks(event):
        state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = state.tasks.get(event['uuid'])

        print('TASK FAILED: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))

    def announce_receive_tasks(event):
        state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = state.tasks.get(event['uuid'])

        print('TASK RECEIVED: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
            'task-failed': announce_failed_tasks,
            'task-received': announce_receive_tasks,
            '*': state.event,
        })
        recv.capture(limit=None, timeout=None, wakeup=True)


# test_monitor(celery)

@celery.task
def while_true():
    while True:
        print("while true 1........")
        while True:
            print("while true 2.......")
            sleep(10)


@celery.task
def count(i):
    if i == 1:
        while True:  # a while loop to achieve what I want to do
            i = i + 1
            sleep(1)
            print(i)
            print('i am counting')



lock = multiprocessing.Lock()
 
@celery.task
def test_lock(x):
    logger.info(str(x) + '---start: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
 
    # 2. 获取锁
    lock.acquire()
    # 3. 保证redis中num对应值的安全性
    # 对x进行任何的操作
    # 4. 释放锁
    lock.release()
