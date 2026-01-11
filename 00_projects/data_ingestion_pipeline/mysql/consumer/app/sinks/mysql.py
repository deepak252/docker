from app.core.database import engine
from app.writers.base import MySQLWritable

class MySQLSink:

    def write(self, data: list[dict], writer: MySQLWritable):
        writer.write_mysql(engine, data)
