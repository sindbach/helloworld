#!/usr/bin/env python
import os
import pytz
import time
import logging
logging.basicConfig()
import grequests
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

logger = logging.getLogger(__name__)

HOME_URL = "http://nonfat-zoologer.mongodb.cc/"

def log_me(response, *args, **kwargs):
    logger.info(response)

def trigger_workerA():
    logger.info("Triggered A")
    path = "worka"
    grequests.map([grequests.get(HOME_URL+path, hooks={'response': log_me})])
    logger.info("finished A")
    return 

def trigger_workerB():
    logger.info("Triggered B")
    path = "workb"
    grequests.map([grequests.get(HOME_URL+path, hooks={'response': log_me})])
    logger.info("finished B")
    return 

if __name__ == "__main__":
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)
    logger.info("Scheduler starts")
    sched.add_job(func=trigger_workerA, trigger='interval', id='scheduled_workerA', max_instances=1, minutes=1, timezone=pytz.utc)
    sched.add_job(func=trigger_workerB, trigger='interval', id='scheduled_workerB', max_instances=1, minutes=3, timezone=pytz.utc)
    sched.start()