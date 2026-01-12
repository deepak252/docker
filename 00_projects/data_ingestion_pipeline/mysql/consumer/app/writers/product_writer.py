from sqlalchemy import text
from app.writers.base import MySQLWritable

class ProductWriter(MySQLWritable):
    def write_mysql(self, engine, records):
        with engine.begin() as conn:
            conn.execute(
                text("""
                INSERT INTO products (
                  company_id,
                  media_channel_id,
                  country_id,
                  title,
                  description,
                  category,
                  start_date,
                  end_date,
                  budget
                )
                VALUES (
                  :company_id,
                  :media_channel_id,
                  :country_id,
                  :title,
                  :description,
                  :category,
                  :start_date,
                  :end_date,
                  :budget
                )
                """),
                records
            )
