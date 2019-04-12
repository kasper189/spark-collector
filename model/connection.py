"""A.
"""
import logging


LOGGER = logging.getLogger()


class Connector(object):

    def __init__(self, server, port, user=None, password=None):
        LOGGER.info("Creating connector with %s", server)
        self._server = server
        self._port = port
        self._user = user
        self._password = password


