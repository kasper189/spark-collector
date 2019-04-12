"""A.
"""
import model.stage
import requests
import logging

LOGGER = logging.getLogger()


def count_stages(connector, application):
    query = 'https://%s:%s/api/v1/applications/application_%s/stages' % (connector._server, connector._port, application._id)
    LOGGER.info("Retrieving number of stages for query: %s", query)

    response = requests.get(query, verify=False)
    return len(response.json())


def retrieve(connector, application, stage_map, id):
    query = 'https://%s:%s/api/v1/applications/application_%s/stages/%s' % (connector._server,
                                                                            connector._port,
                                                                            application._id,
                                                                            id)
    LOGGER.info("Retrieving stage with id: %s", id)
    LOGGER.info("Running query: %s", query)

    response = requests.get(query, verify=False)
    last_attempt = response.json()[-1]
    import json
    LOGGER.debug("Received: %s", json.dumps(last_attempt))
    stage = model.stage.Stage(id, last_attempt['attemptId'], last_attempt['status'],
                              last_attempt['executorCpuTime'], last_attempt['inputBytes'])
    stage_map[id] = stage
    return stage_map
