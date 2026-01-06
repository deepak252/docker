from sqlalchemy import Column, Integer, String, DateTime, func
from app.core.database import Base

# ---------------------------------------------------------
# Country ORM model
# ---------------------------------------------------------
# Represents the "countries" table in the database.
# Inherits from the SQLAlchemy declarative Base class.
class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True) # auto-incremented integer
    name = Column(String(100), unique=True, index=True, nullable=False)
    iso_code = Column(String(2), unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
