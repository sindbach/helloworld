#!/usr/bin/env python
import pytz
import logging
logging.basicConfig()
import grequests
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler(daemon=True)

HOME_URL = "http://nonfat-zoologer.mongodb.cc/"

def trigger_workerA():
    path = "worka"
    grequests.map([grequests.get(HOME_URL+path)])
    return 

def trigger_workerB():
    path = "workb"
    grequests.map([grequests.get(HOME_URL+path)])
    return 

if __name__ == "__main__":
    sched.add_job(func=trigger_workerA, trigger='interval', id='scheduled_workerA', max_instances=1, minutes=3, timezone=pytz.utc)
    sched.add_job(func=trigger_workerB, trigger='interval', id='scheduled_workerB', max_instances=1, minutes=5, timezone=pytz.utc)
    sched.start()