#!/usr/bin/env python 
import pytz
import logging
logging.basicConfig()
import os 
import time 
from flask import Flask
app = Flask(__name__)
from apscheduler.schedulers.background import BackgroundScheduler
sched = BackgroundScheduler()

@app.route('/')
def index():
    app.logger.info("manual request")
    return "1"

@app.route('/worka')
def scheduled_workerA():
    app.logger.info("scheduled worker A")
    time.sleep(30)
    app.logger.info("completed A")
    return "2"

@app.route('/workb')
def scheduled_workerB():
    app.logger.info("scheduled worker B")
    time.sleep(60)
    app.logger.info("completed B")
    return "3"


if __name__ == '__main__':
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    
    app.logger.info("Scheduler starts ...")
    sched.add_job(func=scheduled_workerA, trigger='interval', id='scheduled_workerA', max_instances=1, minutes=1, timezone=pytz.utc)
    sched.add_job(func=scheduled_workerB, trigger='interval', id='scheduled_workerB', max_instances=1, minutes=3, timezone=pytz.utc)
    sched.start()

    app.run(host='0.0.0.0', port=80)

