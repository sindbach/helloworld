#!/usr/bin/env python 
import logging
import os 
import ssl 
from flask import Flask
from flask import render_template
from pymongo import MongoClient, DESCENDING

app = Flask(__name__)

DB_CONN = MongoClient(os.environ.get('DATABASE_URL'), ssl_cert_reqs=ssl.CERT_NONE)
try:
    COLLECTION = DB_CONN.support_gg.test
except Exception, ex: 
    raise Exception("Failed to fetch collection : %s" % ex)

@app.route('/2')
def index():
    app.logger.info("app 2 is requested")
    documents = COLLECTION.find({}, sort=[('_id', DESCENDING)]).limit(2)
    return render_template('index.html', documents=documents)

if __name__ == '__main__':
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    app.run(host='0.0.0.0', port=80)

