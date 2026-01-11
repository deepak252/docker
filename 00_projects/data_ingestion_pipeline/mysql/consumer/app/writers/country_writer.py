from sqlalchemy import text
from app.writers.base import MySQLWritable, ElasticWritable

class CountryWriter(MySQLWritable, ElasticWritable):

    def write_mysql(self, engine, records):        
        with engine.begin() as conn:
            conn.execute(
                text("""
                INSERT INTO countries (name, iso_code)
                VALUES (:name, :iso_code)
                ON DUPLICATE KEY UPDATE
                  name = VALUES(name)
                """),
                records
            )

    def write_elastic(self, client, records):
        pass
    # def write_elastic(self, client, records):
    #     for r in records:
    #         client.index(index="users", document=r)
