from gevent import monkey
monkey.patch_all() 

from gevent.pywsgi import WSGIServer
from flask_app import app 

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    logging.info(f"Starting Gevent WSGI server on {host}:{port}")
    http_server = WSGIServer((host, port), app)
    http_server.serve_forever()    