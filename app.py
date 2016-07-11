#!/usr/bin/env python 
import atexit
from os import environ

from flask import Flask
from flask import render_template
from apscheduler.scheduler import Scheduler

app = Flask(__name__)

cron = Scheduler(daemon=True)
cron.start()


@app.route('/')
def index():
    return render_template('index.html')

@cron.interval_schedule(minutes=3)
def scheduled_worker():
    print "Interval schedule being called"

atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)