# Adapter is intended to wrap to-be-injected interface to make it work with our
# existing code.

# Using both with Dependency Injection let us to create versatile code base
# (i.e. without need to alter the existing code to support new interfaces).

# Delete this and do my own

import socket

class SocketWriter(object):

    def __init__(self, ip, port):
        self._socket = socket.socket(socket.AF_INET,
                                     socket.SOCK_DGRAM)
        self._ip = ip
        self._port = port

    def write(self, message):
        self._socket.send(message, (self._ip, self._port))

def log(message, destination):
    destination.write('[{}] - {}'.format(datetime.now(), message))

upd_logger = SocketWriter('1.2.3.4', '9999')
log('Something happened', upd_logger)
