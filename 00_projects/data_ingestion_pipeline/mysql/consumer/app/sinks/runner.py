from app.sinks.mysql import MySQLSink
from app.sinks.elastic import ElasticSink
from app.writers.base import MySQLWritable, ElasticWritable
from app.utils.logger import get_logger

logger = get_logger(__name__)

class SinkRunner:
    def __init__(self):
        self.mysql = MySQLSink()
        self.elastic = ElasticSink()

    def run(self, writer, payloads: list[dict]):
        if isinstance(writer, MySQLWritable):
            logger.info("Executing MySQL write for %d records", len(payloads))
            self.mysql.write(payloads, writer)

        if isinstance(writer, ElasticWritable):
            logger.info("Executing Elastic write for %d records", len(payloads))
            self.elastic.write(payloads, writer)
