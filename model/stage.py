"""A.
"""
import logging


LOGGER = logging.getLogger()


class Stage(object):

    def __init__(self, id, attempt, status, cpu_time, input_bytes):
        self._id = id
        self._attempt = attempt
        self._status = status
        self._cpu_time = cpu_time
        self._input_bytes = input_bytes
