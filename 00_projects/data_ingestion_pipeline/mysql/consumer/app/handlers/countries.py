# app/handlers/countries.py
from app.handlers.base import BaseHandler
from app.writers.mysql_writer import MySQLWriter


class CountryHandler(BaseHandler):
    def __init__(self):
        self.mysql = MySQLWriter()

    def handle(self, payload: dict):
        """
        payload:
        {
          "name": "India",
          "iso_code": "IN"
        }
        """
        self.mysql.upsert_country(payload)
