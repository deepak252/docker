from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Create database engine - manages database connection
engine = create_engine(settings.DATABASE_URL)

# Session factory for DB operations
# SessionLocal will generate new Session objects for each request.
# autoflush=False → SQLAlchemy will not automatically flush changes
# autocommit=False → You must explicitly call commit() after changes
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for ORM models
# All SQLAlchemy ORM models will inherit from this base.
Base = declarative_base()


# ---------------------------------------------------------
# Dependency for FastAPI routes
# ---------------------------------------------------------
# get_db() provides a database session for each request.
# It ensures the session is created at request start and properly closed after the response is sent.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # Ensures the connection is returned to the pool.
        db.close()