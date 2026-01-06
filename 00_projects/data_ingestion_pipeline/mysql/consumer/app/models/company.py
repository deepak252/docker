from sqlalchemy import Column, Integer, String, DateTime, BigInteger, ForeignKey, func
from app.core.database import Base

# ---------------------------------------------------------
# Company ORM model
# ---------------------------------------------------------
# Represents the "companies" table in the database.
# Inherits from the SQLAlchemy declarative Base class.
class Company(Base):
    __tablename__ = "companies"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    industry = Column(String(100), nullable=True)
    country_id = Column(BigInteger, ForeignKey("countries.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # optional relationship if you have Country model
    # country = relationship("Country", back_populates="companies")

# In Country model you would add:
# companies = relationship("Company", back_populates="country")