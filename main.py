import os

from src._shared.constants import ENV
from src._shared.server import Server
from src._shared.service import Service

if __name__ == '__main__':
    service = Service()
    s = Server('scrap-produtos', service)
    port = int(ENV.FLASK_PORT)
    s.server.app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
        threaded=True
    )