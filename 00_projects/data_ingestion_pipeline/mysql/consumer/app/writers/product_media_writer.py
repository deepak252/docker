from sqlalchemy import text
from app.writers.base import MySQLWritable

class ProductMediaWriter(MySQLWritable):
    def write_mysql(self, engine, records):
        with engine.begin() as conn:
            conn.execute(
                text("""
                INSERT INTO product_media (
                  product_id,
                  media_type,
                  media_url
                )
                VALUES (
                  :product_id,
                  :media_type,
                  :media_url
                )
                """),
                records
            )
