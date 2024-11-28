from shared.environment import Environment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shared.models import Base

# Create engine
engine = create_engine(Environment.DATABASE_URL)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
