from sqlalchemy import Column, Integer, String, DateTime, func
from app.core.database import Base

# ---------------------------------------------------------
# MediaChannel ORM model
# ---------------------------------------------------------
# Represents the "media_channels" table in the database.
# Inherits from the SQLAlchemy declarative Base class.
class MediaChannel(Base):
    __tablename__ = "media_channels"

    id = Column(Integer, primary_key=True, index=True) # auto-incremented integer
    name = Column(String(100), unique=True, index=True, nullable=False)
    type = Column(String(50),  nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
