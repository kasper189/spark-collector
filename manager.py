"""A.
"""
import base64
import command.parser as cparser
import model.application
import model.connection

import scraper.status
import scraper.stage

from html import HTML

import logging

LOGGER = logging.getLogger()


def retrieve():
    arguments = cparser.parse_input_parameters()
    application = model.application.Application(arguments.appId)
    connector = model.connection.Connector(arguments.server, arguments.port)

    application.set_status(
        scraper.status.retrieve(connector, application)
    )

    number_of_stages = scraper.stage.count_stages(connector, application)
    LOGGER.info("Number of stages: %s", number_of_stages)

    stage_map = {}
    for stage in xrange(number_of_stages - 1):
        LOGGER.info("Analysing stage: %s", stage)
        scraper.stage.retrieve(connector, application, stage_map, stage)
    return number_of_stages, stage_map


def build_table(stages, map):
    header_row = ['id', 'attempt', 'status', 'cpu_time', 'input_bytes']

    html_code = HTML()
    table = html_code.table(border='1')
    row = table.tr
    for header in header_row:
        row.td(header)

    for i in range(stages - 1):
        inner_row = table.tr
        inner_row.td(str(map[i]._id))
        inner_row.td(str(map[i]._attempt))
        inner_row.td(str(map[i]._status))
        inner_row.td(str(map[i]._cpu_time))
        inner_row.td(str(map[i]._input_bytes))

    print html_code


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    number_of_stages, stage_map = retrieve()
    build_table(number_of_stages, stage_map)
