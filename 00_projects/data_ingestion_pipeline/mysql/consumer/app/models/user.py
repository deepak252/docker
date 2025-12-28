from sqlalchemy import Column, Integer, String, DateTime, func
from app.core.database import Base

# ---------------------------------------------------------
# User ORM model
# ---------------------------------------------------------
# Represents the "users" table in the database.
# Inherits from the SQLAlchemy declarative Base class.
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) # auto-incremented integer
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
