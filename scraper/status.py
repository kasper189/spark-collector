"""A.
"""
import requests
import logging

LOGGER = logging.getLogger()


def retrieve(connector, application):
    query = 'https://%s:%s/api/v1/applications/application_%s' % (connector._server, connector._port, application._id)
    LOGGER.info("Retrieving status for query: %s", query)

    response = requests.get(query, verify=False)
    return response.json()['attempts'][-1]['completed']
