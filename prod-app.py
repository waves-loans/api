from app import app
from gevent.pywsgi import WSGIServer
from os import getenv
from gevent import monkey


monkey.patch_all()


http_server = WSGIServer(('0.0.0.0', int(getenv('FLASK_RUN_PORT'))), app)
http_server.serve_forever()
