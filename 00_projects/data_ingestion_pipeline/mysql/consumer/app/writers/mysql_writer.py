# app/writers/mysql_writer.py
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import SessionLocal


class MySQLWriter:

    def upsert_country(self, data: dict):
        session: Session = SessionLocal()
        print("upsert_country", data)

        try:
            session.execute(
                text("""
                INSERT INTO countries (name, iso_code)
                VALUES (:name, :iso_code)
                ON DUPLICATE KEY UPDATE
                  name = VALUES(name)
                """),
                {
                    "name": data["name"],
                    "iso_code": data["iso_code"],
                }
            )
            session.commit()

        except Exception as e:
            print("ERROR upsert_country - ", e)
            session.rollback()
            raise

        finally:
            session.close()
