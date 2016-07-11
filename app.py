#!/usr/bin/env python 
import pytz
import logging

from flask import Flask
from flask import render_template
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

sched = BackgroundScheduler(daemon=True)

@app.route('/')
def index():
    app.logger.info("index is requested")
    return render_template('index.html')

def scheduled_worker():
    app.logger.info("scheduled worker")
    index()

if __name__ == '__main__':
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    sched.add_job(scheduled_worker, 'interval', id='scheduled_worker', minutes=60, timezone=pytz.utc)
    sched.start()
    app.run(host='0.0.0.0', port=80)

