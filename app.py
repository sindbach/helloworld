#!/usr/bin/env python 
import atexit
from os import environ

from flask import Flask
from flask import render_template
from apscheduler.schedulers.blocking import BlockingScheduler

app = Flask(__name__)

sched = BlockingScheduler()

@app.route('/')
def index():
    return render_template('index.html')

@sched.scheduled_job('cron', id='scheduled', minutes=3)
def scheduled_worker():
    print "Interval schedule being called"

sched.start()

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80)