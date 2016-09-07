#!/usr/bin/env python
import pytz
import logging
logging.basicConfig()
import grequests
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler(daemon=True)

logger = logging.getLogger(__name__)

HOME_URL = "http://nonfat-zoologer.mongodb.cc/"

def trigger_workerA():
    logger.info("Triggered A")
    path = "worka"
    grequests.map([grequests.get(HOME_URL+path)])
    logger.info("triggered A")
    return 

def trigger_workerB():
    logger.info("Triggered B")
    path = "workb"
    grequests.map([grequests.get(HOME_URL+path)])
    logger.info("Completed A")
    return 

if __name__ == "__main__":
    sched.add_job(func=trigger_workerA, trigger='interval', id='scheduled_workerA', max_instances=1, minutes=3, timezone=pytz.utc)
    sched.add_job(func=trigger_workerB, trigger='interval', id='scheduled_workerB', max_instances=1, minutes=5, timezone=pytz.utc)
    sched.start()