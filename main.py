import os

from _shared.server import Server
from _shared.service import Service

if __name__ == '__main__':
    service = Service()
    s = Server('bcb-ptax', service)
    port = int(os.environ.get('PORT', 5000))
    s.server.app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
        threaded=True
    )