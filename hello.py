from flask import Flask
import os
import logging

app = Flask(__name__)

# log time
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

backend_network = os.environ.get('BACKEND_NETWORK', '0.0.0.0')
backend_port = os.environ.get('BACKEND_PORT', '5000')


@app.route('/')
def hello():
    return 'Hello, PXL!'


if __name__ == "__main__":
    logging.info('starting wholesome backend server with love on ' +
                 backend_network + ' port ' + backend_port)
    app.run(host=backend_network, port=backend_port)
