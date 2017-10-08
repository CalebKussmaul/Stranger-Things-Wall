#!/usr/bin/env python2

import connexion
from gevent.wsgi import WSGIServer

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'Stranger messages holder'})
    #app.run(threaded=True, port=8080)
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()
