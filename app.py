#!/usr/bin/env python 
import pytz
import logging
logging.basicConfig()
import os 
import ssl 
from flask import Flask
from flask import render_template
from apscheduler.schedulers.blocking import BlockingScheduler
from pymongo import MongoClient, DESCENDING

app = Flask(__name__)

#DB_CONN = MongoClient(os.environ.get('DATABASE_URL'), ssl_cert_reqs=ssl.CERT_NONE)
#try:
#    COLLECTION = DB_CONN.support_gg.test
#except Exception, ex: 
#    raise Exception("Failed to fetch collection : %s" % ex)

sched = BlockingScheduler(daemon=True)

@app.route('/')
def index():
    app.logger.info("app 1 is requested")
    #documents = COLLECTION.find({}, sort=[('_id', DESCENDING)]).limit(2)
    #return render_template('index.html', documents=documents)

def scheduled_worker2():
    app.logger.info("scheduled worker 2")

def scheduled_worker():
    app.logger.info("scheduled worker")
    index()
    return

if __name__ == '__main__':
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    sched.add_job(scheduled_worker, 'interval', id='scheduled_worker', minutes=3, timezone=pytz.utc)
    sched.add_job(scheduled_worker2, 'interval', id='scheduled_worker2', minutes=5, timezone=pytz.utc)
    sched.start()
    app.run(host='0.0.0.0', port=80)

