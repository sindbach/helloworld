#!/usr/bin/env python 
import logging
logging.basicConfig()
import os  
from flask import Flask
import pymongo
import ssl 

app = Flask(__name__)

@app.route('/')
def index():
    app_db = mongo_client[os.environ.get('DATABASE_NAME')]
    cursor = app_db[os.environ.get('DATABASE_COLL')].find({}, sort=[("start", pymongo.DESCENDING)]).limit(5)
    for c in cursor: 
        app.logger.info(c)
    return 

if __name__ == '__main__':
    mongo_client = pymongo.MongoClient(os.environ.get(DATABASE_URL), ssl_cert_reqs=ssl.CERT_NONE)
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    app.run(host='0.0.0.0', port=80, threaded=True)

