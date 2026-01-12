from sqlalchemy import text
from app.writers.base import MySQLWritable

class CompanyWriter(MySQLWritable):
    def write_mysql(self, engine, records):
        with engine.begin() as conn:
            conn.execute(
                text("""
                INSERT INTO companies (name, industry, country_id)
                VALUES (:name, :industry, :country_id)
                ON DUPLICATE KEY UPDATE
                  industry = VALUES(industry),
                  country_id = VALUES(country_id)
                """),
                records
            )
