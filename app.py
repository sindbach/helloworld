#!/usr/bin/env python 
import logging
logging.basicConfig()
import os 
import time 
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    app.logger.info("manual request")
    return "1"

@app.route('/workb')
def scheduled_workerB():
    app.logger.info("scheduled worker B")
    time.sleep(10)
    app.logger.info("completed B")
    return "2"

@app.route('/worka')
def scheduled_workerA():
    app.logger.info("scheduled worker A")
    time.sleep(10)
    app.logger.info("completed A")
    return "3"

if __name__ == '__main__':
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    app.run(host='0.0.0.0', port=80)

