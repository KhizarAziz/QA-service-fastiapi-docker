# Importing database stuff from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

# This is the path to our database file
DATABASE_URL = "sqlite:///./knowledge_base.db"

# This line creates a 'connection' to our database
engine = create_engine(DATABASE_URL)

# This makes a 'session' to talk to our database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This helps us create tables in our database
Base: DeclarativeMeta = declarative_base()
