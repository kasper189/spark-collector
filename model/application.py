"""A.
"""
import logging


LOGGER = logging.getLogger()


class Application(object):

    def __init__(self, application_id):
        LOGGER.info("Creating application with id %s", application_id)
        self._id = application_id
        self._status = 'running'

    def set_status(self, status):
        LOGGER.info("The application is completed: %s", status)
        self._status = status


