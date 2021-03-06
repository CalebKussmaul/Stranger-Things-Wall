#!/usr/bin/env python2

import connexion
from gevent.wsgi import WSGIServer
from settings import settings

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'Stranger messages holder'})
    http_server = WSGIServer(('', settings.server_port), app)
    http_server.serve_forever()
