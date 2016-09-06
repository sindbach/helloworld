#!/usr/bin/env python
import pytz
import logging
import urllib.request
logging.basicConfig()
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler(daemon=True)


if __name__ == "__main__":
    sched.add_job(func=urllib.request.urlopen("/worka"), trigger='interval', id='scheduled_workerA', max_instances=1, minutes=3, timezone=pytz.utc)
    sched.add_job(func=urllib.request.urlopen("/workb"), trigger='interval', id='scheduled_workerB', max_instances=1, minutes=5, timezone=pytz.utc)
    sched.start()