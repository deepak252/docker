from app.writers.base import ElasticWritable

class ElasticSink:

    def write(self, records, writer: ElasticWritable):
        pass
        # writer.write_elastic(self.client, records)
