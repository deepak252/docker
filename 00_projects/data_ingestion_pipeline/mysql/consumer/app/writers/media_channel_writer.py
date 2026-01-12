from sqlalchemy import text
from app.writers.base import MySQLWritable

class MediaChannelWriter(MySQLWritable):
    def write_mysql(self, engine, records):
        with engine.begin() as conn:
            conn.execute(
                text("""
                INSERT INTO media_channels (name, type)
                VALUES (:name, :type)
                """),
                records
            )
