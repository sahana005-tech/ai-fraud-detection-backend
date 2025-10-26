from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Path to local SQLite database file
SQLALCHEMY_DATABASE_URL = "sqlite:///./fraud_demo.db"

# Engine handles the actual database connection
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal is used by FastAPI routes to talk to the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the parent class for all table models
Base = declarative_base()
