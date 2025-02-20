from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your actual database URL
DATABASE_URL = "postgresql://postgres:postgres@localhost/url_shortener"

# Set up the connection to the database
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Set up a base class for your models
Base = declarative_base()


# Define your models
class UrlMapping(Base):
    __tablename__ = "url_mapping"

    id = Column(Integer, primary_key=True)
    original_url = Column(String, nullable=False)
    short_id = Column(String, unique=True)


# Create the table in the database
Base.metadata.create_all(bind=engine)
