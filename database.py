from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Define database file (SQLite database)
SQLALCHEMY_DATABASE_URL = "sqlite:///./statista.db"

# Define database using postgres
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/statista_db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
