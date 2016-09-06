#!/usr/bin/env python
import pytz
import logging
import requests
logging.basicConfig()
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler(daemon=True)


if __name__ == "__main__":
    sched.add_job(func=requests.get("http://nonfat-zoologer.mongodb.cc/worka"), trigger='interval', id='scheduled_workerA', max_instances=1, minutes=3, timezone=pytz.utc)
    sched.add_job(func=requests.get("http://nonfat-zoologer.mongodb.cc/workb"), trigger='interval', id='scheduled_workerB', max_instances=1, minutes=5, timezone=pytz.utc)
    sched.start()